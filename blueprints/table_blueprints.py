from flask import Blueprint
from flask import request

from controller.table_controller import TableController

table_blueprints = Blueprint('table_blueprints', __name__)
table_controller = TableController()


@table_blueprints.route("/table/all", methods=['GET'])
def get_all_table():
    response = table_controller.index()
    return response,  200


@table_blueprints.route("/table/<string:id_>", methods=['GET'])
def get_table_by_id(id_):
    response = table_controller.Show(id_)
    return response, 200


@table_blueprints.route("/table/insert", methods=['POST'])
def insert_table():
    table = request.get_json()
    response = table_controller.Create(table)
    return response, 201


@table_blueprints.route("/table/update/<string:id_>", methods=['PATCH'])
def update_table(id_):
    table = request.get_json()
    response = table_controller.Update(id_, table)
    return response, 201


@table_blueprints.route("/table/delete/<string:id_>", methods=['DELETE'])
def delete_table(id_):
    response = table_controller.Delete(id_)
    return response, 204
