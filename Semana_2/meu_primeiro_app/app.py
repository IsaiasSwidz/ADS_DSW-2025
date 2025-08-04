from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    nome_usuario = "visitantes"
    return render_template('pagina.html', usuario=nome_usuario)