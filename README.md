1. Crear archivo Pipfile
2. En la terminal o consola ejecutamos el siguiente comando:
```shell
pipenv shell
```
3. Install flask 
```shell
pipenv install flask
```
4. Crear un archivo llamado app.py
```python
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

```