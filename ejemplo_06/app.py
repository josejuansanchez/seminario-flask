from flask import Flask

app = Flask(__name__)

@app.get('/')
def handle_get():
    return "Petición por GET"

@app.post('/')
def handle_post():
    return "Petición por POST"

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)