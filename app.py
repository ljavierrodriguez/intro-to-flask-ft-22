from flask import Flask, jsonify, request, json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/')
def main():
    data = {
        "status": "Server Up"
    }
    return jsonify(data), 200

@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method == 'GET':
        return "Usando metodo GET"
    if request.method == 'POST':
        return "Usando metodo POST"
    if request.method == 'PUT':
        return "Usando metodo PUT"
    if request.method == 'DELETE':
        return "Usando metodo DELETE"
    
    
@app.route("/enviando-data/<usuario>/<int:id>", methods=['POST', 'PUT'])
def enviando_data(usuario, id):
    
    # recibiendo informacion por query string
    query = request.args
    print(query)
    
    filter = query['filter']
    value = query['value']
    
    print(filter)
    print(value)
    
    # Recibiendo datos
    '''
    data = request.data
    data = json.loads(data)
    return jsonify(data)
    '''
    
    # Recibiendo datos en formato json
    # data = request.get_json()
    # print(data["saludo"])
    # return jsonify(data)
    
    #saludo = request.json.get("saludo")
    #print(saludo)
    #return jsonify(saludo)
    
    username = request.form["username"]
    password = request.form["password"]
    
    return jsonify({ "username": username, "password": password, "usuario": usuario, "id": id })


if __name__ == '__main__':
    app.run()