from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL base de la API en MockAPI
base_url = "https://xxxxxxxxxxxxxxxxxxx.mockapi.io/api/v1/IoTCarStatus"


# GET - Leer todos los registros o uno en específico
@app.route('/car-status', methods=['GET'])
def get_car_status():
    record_id = request.args.get('id')  # Recibir un parámetro opcional "id"

    if record_id:
        response = requests.get(f"{base_url}/{record_id}")
    else:
        response = requests.get(base_url)

    return jsonify(response.json())


# POST - Crear un nuevo registro
@app.route('/car-status', methods=['POST'])
def create_car_status():
    data = request.json  # Recibir los datos en formato JSON desde el cliente
    response = requests.post(base_url, json=data)
    return jsonify(response.json())


# PUT - Actualizar un registro existente
@app.route('/car-status/<int:id>', methods=['PUT'])
def update_car_status(id):
    data = request.json  # Recibir los datos actualizados en formato JSON
    response = requests.put(f"{base_url}/{id}", json=data)
    return jsonify(response.json())


# DELETE - Eliminar un registro existente
@app.route('/car-status/<int:id>', methods=['DELETE'])
def delete_car_status(id):
    response = requests.delete(f"{base_url}/{id}")
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
