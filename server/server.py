from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    arg1 = data['arg1']
    arg2 = data['arg2']
    operation = data['operation']

    # Проверяем, что аргументы числа
    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
    except ValueError:
        return jsonify({'error': 'Аргументы должны быть числами'})

    if operation == '+':
        result = arg1 + arg2
    elif operation == '-':
        result = arg1 - arg2
    elif operation == '*':
        result = arg1 * arg2
    elif operation == '/':
        if arg2 == 0:
            return jsonify({'error': 'Деление на ноль невозможно'})
        result = arg1 / arg2
    else:
        return jsonify({'error': 'Неподдерживаемая операция'})

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=False)
