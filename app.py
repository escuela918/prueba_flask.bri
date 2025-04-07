from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def main():
    url_hola =  url_for("hello")
    url_dado = url_for ("dados", caras=8)
    url_logo= url_for("static", filename="logo.jpg")
    return f"""
    <a href="{url_hola}">saludar</a>
    <br>
    <a href="{url_dado}">tirar</a>
    <br>
    <a href="{url_logo}">logo</a>
    
    
    """


@app.route('/saludar')
def hello():
    return 'Hello, World!'

@app.route('/gsdh')
def gsdh():
    return 'dtyjj'

@app.route('/tirar/<int:caras>')
def dados(caras):
    from random import randint
    ca = randint(1, caras)
    return f'<p>tire un dado de {caras}, salio {ca}<p>'


@app.route('/sumar/<int:n1>/<int:n2>')
def suma(n1,n2):
    s = n1 + n2
    return f'<p>{n1} + {n2} = {s}<p>'

@app.route('/nombre/nombre/<string:nombre>')
def nombre():
    return f'<p>hola {nombre}<p>'

    
    
