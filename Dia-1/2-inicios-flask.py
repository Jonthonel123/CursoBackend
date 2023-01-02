from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app=app, origins=['http://127.0.0.1:5500'], methods=['GET', 'POST'])

usuarios = [
    {
        'nombre': 'Carlos',
        'apellido': 'Requena'
    },
    {
        'nombre': 'Manuel',
        'apellido': 'Morales'
    },
    {
        'nombre': 'Pierina',
        'apellido': 'Nicho'
    },
]


@app.route('/')
def inicio():
    return 'Hola desde Flask'


@app.route('/mostrar-hora', methods=['GET', 'POST'])
def mostrarHora():
    print(request.method)
    if request.method == 'GET':
        return {
            'content': 'Me hiciste Get'
        }
    elif request.method == 'POST':
        return {
            'content': 'Me hiciste Post'
        }
    return {
        'content': '22:50:15'
    }


@app.route('/usuarios', methods=['GET', 'POST'])
def gestionUsuarios():
    if request.method == 'GET':
        # Devolvemos los usuarios
        return {
            'message': 'Los usuarios son',
            'content': usuarios
        }
    elif request.method == 'POST':
        # Agregar un nuevo usuario
        # print(request.data)
        print(request.get_json())
        data = request.get_json()
        usuarios.append(data)
        return {
            'message': 'Usuario agregado exitosamente'
        }


app.run(debug=True)
