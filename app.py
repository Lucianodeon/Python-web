import datetime
from flask import Flask, render_template, request

app = Flask(__name__)



#@app.route("/")#cuando app routea a default va a index
#def index():
#    return "hello world"
#para cambiar el nombre de este archivo y que flask funcione
#tengo que hacer en el terminal "export FLASK_APP=nombre.py"
#@app.route("/lucho")
#def lucho():
#    return "que haces papa, luchito kpo"
#para agregar rutas reiniciar flask



@app.route("/")
def index():
    return render_template("index.html")
#para Flask necesito poner el css en una carperta static junto a las imagines y js
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/nuevoano")
def nuevoano():
    now= datetime.datetime.now()
    new_year= now.month==1 and now.day==1
    #new_year=True si quiero que sea ano nuevo cuando no es
    return render_template("ano.html",new_year=new_year)

@app.route("/lista")
def lista():
    names=["luchi","bob","alice"]
    return render_template("name.html", names=names)
@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/hola" , methods=["GET","POST"])
def hola():
    if request.method=="GET":
        return "Por favor completa el formulario"
    name=request.form.get("name")
    return render_template("hola.html", name=name)

notes=[]

@app.route("/note", methods=["GET","POST"])
def note():
    if request.method=="POST":
        note=request.form.get("note")
        notes.append(note)
    return render_template("note.html", notes=notes )


#@app.route("/<string:name>")
#def hello(name):
#    name=name.capitalize()
#    return f"hello,{name}"
