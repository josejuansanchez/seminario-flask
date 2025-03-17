from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "Petición por POST"
    else:
        return "Petición por GET"

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)