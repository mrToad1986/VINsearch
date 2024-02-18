from flask import Flask, jsonify, request

app = Flask(__name__)

cars = {
    "ABC123456": {"brand": "Toyota", "model": "Camry", "year": 2020},
    "XYZ789012": {"brand": "Ford", "model": "Focus", "year": 2019},
    "LMN345678": {"brand": "Honda", "model": "Civic", "year": 2021}
}

@app.route('/api/v1/car/<vin>', methods=['GET'])
def get_car(vin):
    car = cars.get(vin)

    if car:
        return jsonify(car), 200
    else:
        return jsonify(message="VIN не найден"), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)