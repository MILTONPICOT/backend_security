from flask import Blueprint
from flask import request

from controller.politicalParty_controller import PoliticalPartyController

politicalParty_blueprints = Blueprint('politicalParty_blueprints', __name__)
politicalParty_controller = PoliticalPartyController()


@politicalParty_blueprints.route("/politicalParty/all", methods=['GET'])
def get_all_political_party():
    response = politicalParty_controller.index()
    return response, 200


@politicalParty_blueprints.route("/politicalParty/<string:id_>", methods=['GET'])
def get_political_party_by_id(id_):
    response = politicalParty_controller.show(id_)
    return response, 200


@politicalParty_blueprints.route("/politicalParty/insert", methods=['POST'])
def insert_political_party():
    politicalParty = request.get_json()
    response = politicalParty_controller.Create(politicalParty)
    return response, 201


@politicalParty_blueprints.route("/politicalParty/update/<string:id_>", methods=['PATCH'])
def update_political_party(id_):
    politicalParty = request.get_json()
    response = politicalParty_controller.Update(id_, politicalParty)
    return response, 201


@politicalParty_blueprints.route("/politicalParty/delete/<string:id_>", methods=['DELETE'])
def delete_political_party(id_):
    response = politicalParty_controller.Delete(id_)
    return response, 204



