# ref: https://stackoverflow.com/questions/28795561/support-multiple-api-versions-in-flask/28797512

from flask import (
    Flask,
    jsonify,
    request
)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World'


@app.route('/v1/questionnaire-food', methods=['POST'])
def questionnaire_food():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')