from flask import Flask

# Creamos una instancia de Flask
app = Flask(__name__)

# Definimos los endpoints de la aplicación
@app.route('/')
def index():
    return '<h1>Hola, mundo!</h1>'

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)