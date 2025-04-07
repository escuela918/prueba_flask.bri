from flask import Flask

app = Flask(__name__)


@app.route('/saludar')
def hello():
    return 'Hello, World!'

@app.route('/gsdh')
def gsdh():
    return 'dtyjj'

@app.route('/tirar/<int:dado>')
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
