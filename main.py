import json
from flask import Flask
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


def load_file_config():
    with open("config.json","r") as config:
        data = json.load(config)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("server running:http//"+data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port') )



