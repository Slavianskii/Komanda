from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    arg1 = data['arg1']
    arg2 = data['arg2']

    arg2IsPercent = False

    operation = data['operation']
    try:
        if '%' in arg1:
            arg1 = float(arg1.strip('%')) / 100
        else:
            arg1 = float(arg1)

        if '%' in arg2:
            arg2IsPercent = True
            arg2 = float(arg2.strip('%')) / 100
        else:
            arg2 = float(arg2)

    except ValueError:
        return jsonify({'error': 'Не верный агрумент'})

    if operation == '+':
        if arg2IsPercent:
            result = arg1 + arg1 * arg2
        else:
            result = arg1 + arg2
    elif operation == '-':
        if arg2IsPercent:
            result = arg1 - arg1 * arg2
        else:
            result = arg1 - arg2
    elif operation == '*':
        result = arg1 * arg2
    elif operation == '/':
        if arg2 == 0:
            return jsonify({'error': 'Деление на ноль невозможно'})
        result = arg1 / arg2
    else:
        return jsonify({'result': 'Неподдерживаемая операция'})

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=False)
