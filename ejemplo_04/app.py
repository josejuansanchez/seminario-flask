from flask import Flask

# Creamos una instancia de Flask
app = Flask(__name__)

# Definimos los endpoints de la aplicación
@app.route('/<string:name>')
def index(name=None):    
    return f"Hola {name}!"

@app.route('/producto/<int:id>')
def producto(id):
    return f"Producto: {id}"

@app.route('/producto/<float:price>')
def precio(price):
    return f"Precio: {price}"

@app.route('/path/<path:subpath>')
def path(subpath):
    return f"Subpath: {subpath}"

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)