from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'quatro&20'

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:cmb110205@localhost/collectionstep'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Produtos(db.Model):
    __tablename__ = 'produtos'
    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rastreio_pedido = db.Column(db.String(50), nullable=False)
    datareceb_prod = db.Column(db.String(20), nullable=False)
    tipo_prod = db.Column(db.String(50), nullable=False)
    desc_prod = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Produto %r>' % self.rastreio_pedido

# Rotas
@app.route("/")
def paginaInicial():
    produtos_cadastrados = Produtos.query.order_by(Produtos.id_produto).all()
    return render_template("index.html", Produtos = produtos_cadastrados  )

@app.route('/cadastrar_prod')
def cadastrar_produto():
    return render_template('cadastrar_produto.html')

@app.route('/adicionar_produto', methods=['POST'])
def adicionar_produto():
    rastreio = request.form['txtRastreio']
    tipo = request.form['txtTipo']
    data = request.form['txtData']
    descricao = request.form['txtDescricao']

    produto_adicionado = Produtos(
        rastreio_pedido=rastreio,
        datareceb_prod=data,
        tipo_prod=tipo,
        desc_prod=descricao
    )

    db.session.add(produto_adicionado)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
