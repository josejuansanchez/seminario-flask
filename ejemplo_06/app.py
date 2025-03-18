from flask import Flask

# Creamos una instancia de Flask
app = Flask(__name__)

# Definimos los endpoints de la aplicación
@app.get('/')
def peticion_get():
    return "Petición por GET"

@app.post('/')
def peticion_post():
    return "Petición por POST"

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)