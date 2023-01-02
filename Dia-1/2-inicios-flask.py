from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Hola desde Flask'


app.run(debug=True)
