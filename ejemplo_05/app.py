from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"Página principal"

@app.errorhandler(404)
def page_not_found(error):
    return f"La página no existe. Error: {error}", 404

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)