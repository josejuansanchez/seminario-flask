from flask import Flask
from flask import request

# Creamos una instancia de Flask
app = Flask(__name__)

# Definimos los endpoints de la aplicación
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "Petición por POST"
    else:
        return "Petición por GET"

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)