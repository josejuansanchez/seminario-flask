from flask import Flask
from flask import abort
from flask import redirect

# Creamos una instancia de Flask
app = Flask(__name__)

# Definimos los endpoints de la aplicación
@app.route('/')
def index():
    #abort(500)
    return f"Página principal"

@app.errorhandler(404)
def page_not_found(error):
    return f"La página no existe. Error: {error}", 404

@app.errorhandler(500)
def server_error(error):
    return f"Error interno en el servidor. Error: {error}", 500

@app.route('/redireccion')
def redireccion():
    return redirect('/')
    #return redirect('/', code=301)

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)