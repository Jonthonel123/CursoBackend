from flask import Flask
from os import environ
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/")
def inicio():
    return "<p>Hola desde el backend</p>"


@app.route("/productos")
def productos():
    lista_productos = [

    ]


app.run(debug=True)
