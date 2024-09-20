from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para el saludo con método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    mensaje = {
        'saludo': '¡Hola, bienvenido a la API!',
        'metodo': 'GET'
    }
    return jsonify(mensaje)

if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug para desarrollo
    app.run(debug=True)
