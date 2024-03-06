from flask import Flask, request, jsonify
from calculator import calculator

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    arg1 = data['arg1']
    arg2 = data['arg2']
    operation = data['operation']

    key, value = calculator(arg1, arg2, operation)
    return jsonify({key: value})


if __name__ == '__main__':
    app.run(debug=False)
