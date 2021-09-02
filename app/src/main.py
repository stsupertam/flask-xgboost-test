from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World 99999'

if __name__ == '__main__':
    app.run(host='0.0.0.0')