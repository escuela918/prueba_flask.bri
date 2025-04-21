
from flask import Flask, url_for, render_template
import sqlite3 

app = Flask(__name__)
def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

db= None 
def abrirconexion():
  global db
  db= sqlite3.connect("instance/datos.sqlite")
  db.row_factory = dict_factory


def cerrarconexion():
  global db
  db.close()
  db=None

@app.route('/test.bd')
def testDB():
    abrirconexion()
    cursor =db.cursor()
    cursor.execute("SELECT COUNT(*) AS cant FROM usuarios ;")
    res=cursor.fetchone()
    registros =res["cant"]
    cerrarconexion()
    return f"hay{registros} registros en la tabla usuario"

@app.route('/crear_usuario')
def testcrear ():
    nombre=leandro
    email= leandro@etec.uba.ar
    abrirconexion()
    cursor =db.cursor()
    consulta = "INSERT INTO usuarios(usuaario, email)"
    cursor.execute(consuta,(nombre,email))
    db.commit
    cerrarconexion()
    return f"registro agregado ({nombre})"


@app.route('/crear_usuario_argumento/<string:usuario>/<string:email>')
def vnuis(usuario, email ):
    abrirconexion()
    cursor =db.cursor()
    consulta = "INSERT INTO usuarios(usuario, email) VALUES (?,?)"
    cursor.execute(consulta,(usuario,email))
    db.commit()
    cerrarconexion()
    return f"registro agregado ({usuario })"

@app.route('/eliminar')
def argumento(usuario, email ):
    abrirconexion()
    cursor =db.cursor()
    consulta = "INSERT INTO usuario(usuario, email) VALUES (?,?);"
    cursor.execute(consulta,(usuario,email))
    db.commit()
    cerrarconexion()
    return f"registro agregado ({usuario })"

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
    
@app.route("/mostrar-datos-plantilla/<int:id>")
def fgsh(id):
    abrirconexion()
    cursor = db.cursor()
    res= cursor.execute("SELECT id, usuario, email, direccion, telefono FROM usuarios WHERE id= ?",(id,))
    res= cursor.fetchone()
    cerrarconexion()
    usuario=None 
    email= None 
    direccion = None 
    telefono=None 
    if res!= None:
        usuario= res['usuario']
        email = res ['email']
        direccion = res['direccion']
        telefono=res['telefono']
    return render_template("datos.html", id=id, usuario=usuario, email=email, direccion= direccion, telefono=telefono )