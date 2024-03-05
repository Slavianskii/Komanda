from flask import jsonify

def calculator(arg1,arg2,operation):
    arg2IsPercent = False
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