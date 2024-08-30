from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(100), nullable=False)
    enunciado = db.Column(db.String(200), nullable=False)
    resposta_correta = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    alternativa1 = db.Column(db.String(100), nullable=False)
    alternativa2 = db.Column(db.String(100), nullable=False)
    alternativa3 = db.Column(db.String(100), nullable=False)
    alternativa4 = db.Column(db.String(100), nullable=False)
    alternativa5 = db.Column(db.String(100), nullable=False)
    resposta_enviada = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"<Questao {self.enunciado}>"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/questoes')
def questoes():
    return render_template("questoes.html", questoes=questoes)

@app.route('/verificar_resposta', methods=['POST'])
def verificar_resposta():
    questao_id = request.form.get('questao_id')
    resposta_enviada = request.form.get('resposta')
    
    # Buscar a questão no banco de dados
    questao = Questao.query.get(questao_id)
    
    if questao:
        # Salva a resposta enviada pelo usuário no banco de dados
        questao.resposta_enviada = resposta_enviada
        db.session.commit()
        
        # Verifica se a resposta está correta
        if resposta_enviada == questao.resposta_correta:
            return "Resposta correta!"
        else:
            return "Resposta incorreta. Tente novamente."
    else:
        return "Questão não encontrada", 404

@app.route('/config')
def config():
    return render_template("config.html")

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        enunciado = request.form['enunciado']
        resposta_correta = request.form['resposta']
        numero = request.form['numero']
        categoria = request.form['categoria']
        alternativa1 = request.form['alternativa1']
        alternativa2 = request.form['alternativa2']
        alternativa3 = request.form['alternativa3']
        alternativa4 = request.form['alternativa4']
        alternativa5 = request.form['alternativa5']
        nova_questao = Questao(enunciado=enunciado, resposta_correta=resposta_correta, numero=numero, categoria=categoria, alternativa1=alternativa1, alternativa2=alternativa2, alternativa3=alternativa3, alternativa4=alternativa4, alternativa5=alternativa5, resposta_enviada="")
        db.session.add(nova_questao)
        db.session.commit()
        return redirect(url_for('confirmado'))  # Redireciona para a página que exibe as questões após a adição
    return render_template("adicionar.html")

@app.route('/confirmado')
def confirmado():
    return render_template("confirmado.html")

@app.route('/editar')
def editar():
    return render_template("editar_1etapa.html")


@app.route('/buscar_questao', methods=['GET', 'POST'])
def buscar_questao():
    numero = request.form['numero']
    questao = Questao.query.filter_by(id=numero).first()
    if questao:
        return redirect(url_for('editar_questao', id=questao.id))
    else:
        return render_template('erro.html', mensagem="Questão não encontrada.")
    return render_template('editar_1etapa.html')

@app.route('/editar_questao/<int:id>', methods=['GET', 'POST'])
def editar_questao(id):
    questao = Questao.query.get_or_404(id)
    if request.method == 'POST':
        questao.enunciado = request.form['enunciado']
        questao.resposta_correta = request.form['resposta_correta']
        db.session.commit()
        return redirect(url_for('confirmado'))
    return render_template('editar_2etapa.html', questao=questao)

@app.route('/excluir', methods=['GET', 'POST'])
def excluir():
    if request.method == 'POST':
        questao_id = request.form.get('questao_id')
        questao = Questao.query.get(questao_id)

        if questao:
            db.session.delete(questao)
            db.session.commit()
            return "Questão excluída com sucesso!"
        else:
            return "Questão não encontrada", 404

    # Se o método for GET, exibe o formulário com as questões
    questoes = Questao.query.all()
    return render_template('excluir.html', questoes=questoes)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

