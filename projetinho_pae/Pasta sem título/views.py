from flask import Flask, render_template, redirect, request
from models import *
from main import db, app

# Rotas 
@app.route("/")
def paginaInicial():
    produtos_cadastrados = Produtos.query.order_by(Produtos.id_produto).all()
    return render_template("index.html", Produtos = produtos_cadastrados  )

@app.route('/cadastrar_prod')
def cadastrar_produto():
    return render_template('cadastrar_produto.html')

@app.route('/login')
def login():
    redirect ('login.html')
    
@app.route('/logar')
def logar():
    email = request.form['txtEmail']
    senha = request.form['txtSenha']
    return redirect ('/')
    
'''@app.route('/registro')
def registro ():
    redirect ('reg.html')

@app.route'''

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
app.run(debug=True)