from flask import Flask, jsonify, request

app = Flask(__name__)

# Método GET - Devuelve un saludo
@app.route('/saludo', methods=['GET'])
def get_saludo():
    mensaje = {
        'mensaje': '¡Hola, este es un saludo desde el método GET!',
        'metodo': 'GET'
    }
    return jsonify(mensaje)

# Método POST - Recibe y muestra un mensaje personalizado
@app.route('/saludo', methods=['POST'])
def post_saludo():
    data = request.json  # Recibe el cuerpo de la petición en formato JSON
    mensaje = {
        'mensaje': f'¡Hola, {data.get("nombre")}! Este es un saludo desde el método POST.',
        'metodo': 'POST'
    }
    return jsonify(mensaje)

# Método PUT - Actualiza un mensaje
@app.route('/saludo', methods=['PUT'])
def put_saludo():
    data = request.json  # Recibe el cuerpo de la petición en formato JSON
    mensaje = {
        'mensaje': f'¡Hola, {data.get("nombre")}! Este es un saludo actualizado desde el método PUT.',
        'metodo': 'PUT'
    }
    return jsonify(mensaje)

# Método DELETE - Confirma la eliminación
@app.route('/saludo', methods=['DELETE'])
def delete_saludo():
    mensaje = {
        'mensaje': '¡El saludo ha sido eliminado con éxito!',
        'metodo': 'DELETE'
    }
    return jsonify(mensaje)

if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug para desarrollo
    app.run(debug=True)
