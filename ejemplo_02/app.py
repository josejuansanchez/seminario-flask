from flask import Flask

# Creamos una instancia de Flask
app = Flask(__name__)

# Definimos los endpoints de la aplicación
@app.route('/')
def index():
    return 'Página principal'

@app.route('/contacto')
def contacto():
    return 'Contacto'

@app.route('/formulario')
def formulario():
    return 'Formulario'

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)