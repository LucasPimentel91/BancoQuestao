from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(200), nullable=False)
    resposta_correta = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)

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

@app.route('/adicionar')
def adicionar():
    nova_questao = Questao(enunciado="Qual a capital da França?", resposta_correta="Paris", categoria="Geografia")
    db.session.add(nova_questao)
    db.session.commit()
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

