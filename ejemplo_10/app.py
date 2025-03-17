from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

# Creamos una instancia de Flask
app = Flask(__name__)

# Definimos los endpoints de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro/', methods=['GET', 'POST'])
def procesar_formulario():
    if request.method == 'POST':
        # Obtenemos los parámetros del formulario
        nombre = request.form['nombre']
        email = request.form['email']

        # Devolvemos los datos a la plantilla
        return render_template('registro.html', nombre=nombre, email=email)
    else:
        return redirect(url_for('index'))

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)