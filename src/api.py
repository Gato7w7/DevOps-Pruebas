from flask import Flask, jsonify, request
from .calculadora import Calculadora

app = Flask(__name__)
calc = Calculadora()

@app.route('/suma', methods=['POST'])
def api_suma():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    resultado = calc.calcular_suma(a, b)
    return jsonify({"resultado": resultado})

@app.route('/historial', methods=['GET'])
def api_historial():
    return jsonify({"historial": calc.obtener_historial()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)