from flask import Flask, render_template

app = Flask(__name__)

'''@app.route('/inicio')
def teste():
    return "<h3>Testando conexão flask...</h3>"'''

@app.route("/adm")
def centralAdministrativo():
    return render_template('adm.html')
@app.route("/")
def paginaIncial():
    return render_template("index.html")
app.run()