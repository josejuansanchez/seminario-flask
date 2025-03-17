from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtenemos los parámetros del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        
        # Devolvemos los datos a la plantilla
        return render_template('index.html', nombre=nombre, email=email)
    else:
        return render_template('index.html')

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)