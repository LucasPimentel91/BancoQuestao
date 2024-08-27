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
def template():
    return render_template("template.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add')
def add_questao():
    nova_questao = Questao(enunciado="Qual a capital da França?", resposta_correta="Paris", categoria="Geografia")
    db.session.add(nova_questao)
    db.session.commit()
    return "Questão adicionada com sucesso!"

@app.route('/questoes')
def exibir_questoes():
    questoes = Questao.query.all()
    return render_template("questoes.html", questoes=questoes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

