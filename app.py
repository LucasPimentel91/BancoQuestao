from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(200), nullable=False)
    resposta_correta = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    alternativa1 = db.Column(db.String(100), nullable=False)
    alternativa2 = db.Column(db.String(100), nullable=False)
    alternativa3 = db.Column(db.String(100), nullable=False)
    alternativa4 = db.Column(db.String(100), nullable=False)
    alternativa5 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Questao {self.enunciado}>"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/questoes', methods=['GET'])
def questoes():
    questoes = Questao.query.all()
    return render_template("questoes.html", questoes=questoes)

@app.route('/config')
def config():
    return render_template("config.html")

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        enunciado = request.form['enunciado']
        resposta_correta = request.form['resposta']
        categoria = request.form['categoria']
        alternativa1 = request.form['alternativa1']
        alternativa2 = request.form['alternativa2']
        alternativa3 = request.form['alternativa3']
        alternativa4 = request.form['alternativa4']
        alternativa5 = request.form['alternativa5']
        nova_questao = Questao(enunciado=enunciado, resposta_correta=resposta_correta, categoria=categoria, alternativa1=alternativa1, alternativa2=alternativa2, alternativa3=alternativa3, alternativa4=alternativa4, alternativa5=alternativa5)
        db.session.add(nova_questao)
        db.session.commit()
        return redirect(url_for('questoes'))  # Redireciona para a página que exibe as questões após a adição
    return render_template("adicionar.html")

@app.route('/editar')
def editar():
    return render_template("editar.html")

@app.route('/excluir')
def excluir():
    return render_template("excluir.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

