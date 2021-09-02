from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'


@app.route('/predict', methods=['POST'])
def xgboost_predict():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')