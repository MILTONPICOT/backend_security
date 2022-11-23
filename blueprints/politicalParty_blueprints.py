from flask import Blueprint
from flask import request

from controllers.politicalpartyController import PoliticalPartyController

politicalparty_blueprints = Blueprint('politicalparty_blueprints', __name__)
politicalparty_controller = PoliticalPartyController()


@politicalparty_blueprints.route("/politicalparty/all", methods=['GET'])
def get_all_politicalparty():
    response = politicalparty_controller.index()
    return response, 200


@politicalparty_blueprints.route("/politicalparty/<string:id_>", methods=['GET'])
def get_politicalparty_by_id(id_):
    response = politicalparty_controller.show(id_)
    return response, 200


@politicalparty_blueprints.route("/politicalparty/insert", methods=['POST'])
def insert_politicalparty():
    politicalparty = request.get_json()
    response = politicalparty_controller.create(politicalparty)
    return response, 201


@politicalparty_blueprints.route("/politicalparty/update/<string:id_>", methods=['PATCH'])
def update_politicalparty(id_):
    politicalparty = request.get_json()
    response = politicalparty_controller.update(id_, politicalparty)
    return response, 201


@politicalparty_blueprints.route("/politicalparty/delete/<string:id_>", methods=['DELETE'])
def delete_politicalparty(id_):
    response = politicalparty_controller.delete(id_)
    return response, 204


