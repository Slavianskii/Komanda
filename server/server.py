from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    arg1 = data['arg1']
    arg2 = data['arg2']


    return jsonify({'result': None})

if __name__ == '__main__':
    app.run(debug=False)
