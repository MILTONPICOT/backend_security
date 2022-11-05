import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidate_blueprints import candidate_blueprints
from blueprints.politicalParty_blueprints import politicalParty_blueprints
from blueprints.results_blueprints import result_blueprints
from blueprints.table_blueprints import table_blueprints

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(candidate_blueprints)
app.register_blueprint(politicalParty_blueprints)
app.register_blueprint(result_blueprints)
app.register_blueprint(table_blueprints)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to software votes G1"}
    return jsonify(response)

#=====config and execution code=====#


def load_file_config():
    with open("config.json", "r") as config:
        data = json.load(config)  # lee el contenido de un archivo json y lo guarda como un diccionario phyton
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))



