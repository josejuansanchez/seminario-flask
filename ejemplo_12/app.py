from flask import Flask
from flask import request
from flask import render_template
from chatbot import Chatbot

# Creamos una instancia de Flask
app = Flask(__name__)

# Creamos una instancia del Chatbot
bot = Chatbot("modelo.keras", "vocabulary.txt", "etiquetas.json")

# Definimos los endpoints de la aplicación
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtenemos los parámetros del formulario
        mensaje = request.form['mensaje']

        # Procesamos el mensaje con el chatbot
        respuesta = bot.procesar_mensaje(mensaje)

        # Devolvemos los datos a la plantilla
        return render_template('index.html', mensaje=mensaje, respuesta=respuesta)
    else:
        return render_template('index.html')

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)