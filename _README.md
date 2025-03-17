# Creación y activación del entorno virtual

**Linux y MacOS**

```bash
# Creamos el entorno virtual
python3.11 -m venv .venv

# Activamos el entorno virtual
source .venv/bin/activate
```

**Windows**

```bash
# Creamos el entorno virtual
py -3.11 -m venv .venv

# Activamos el entorno virtual en PowerShell
.venv\Scripts\Activate.ps1
```

# Instalación de las dependencias de forma manual

```bash
# Instalamos Flask
pip install flask

# Instalamos Tensorflow
pip install tensorflow
```

# Creación del archivo `requeriments.txt`

```bash
pip freeze > requirements.txt
```

Una vez que hemos creado el archivo `requirements.txt`, cuando queramos instalar
las dependencias en otro entorno, sólo tendremos que ejecutar el siguiente
comando:

```bash
pip install -r requirements.txt
```

# ¿Qué es Flask?

Flask es un **micro-framework** escrito en Python que permite crear aplicaciones
web rápidamente de forma sencilla.

Es ideal para pequeños proyectos o prototipos.

# Instalación de Flask

- https://flask-es.readthedocs.io/installation/

# Creación de una aplicación Flask

Vamos a crear un archivo que se llama `app.py` con el siguiente contenido:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

# Ejecución de la aplicación

```bash
python app.py
```

# Referencias

- https://flask-es.readthedocs.io/quickstart/
- https://flask-es.readthedocs.io/tutorial/