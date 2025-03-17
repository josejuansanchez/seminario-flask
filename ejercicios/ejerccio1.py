from flask import Flask
from flask import abort

# Creamos una instancia de Flask
app = Flask(__name__)

@app.route('/admin')
def admin():
    abort(403)

@app.errorhandler(403)
def forbidden(error):
    return f"Error: {error}", 403

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)