from flask import jsonify

def calculator(arg1,arg2,operation):
    arg1IsPercent = False
    arg2IsPercent = False
    try:
        if arg1[-1] == '%':
            arg1IsPercent = True
            arg1 = float(arg1.strip('%')) / 100
        else:
            arg1 = float(arg1)

        if arg2[-1] == '%':
            arg2IsPercent = True
            arg2 = float(arg2.strip('%')) / 100
        else:
            arg2 = float(arg2)

    except ValueError:
        return 'error', 'Не верный агрумент'

    if operation == '+':
        if arg2IsPercent and not arg1IsPercent:
            result = arg1 + arg1 * arg2
        else:
            result = arg1 + arg2
    elif operation == '-':
        if arg2IsPercent and not arg1IsPercent:
            result = arg1 - arg1 * arg2
        else:
            result = arg1 - arg2
    elif operation == '*':
        result = arg1 * arg2
    elif operation == '/':
        if arg2 == 0:
            return 'error', 'Деление на ноль невозможно'
        result = arg1 / arg2
    else:
        return 'error', 'Неподдерживаемая операция'

    return 'result', result
