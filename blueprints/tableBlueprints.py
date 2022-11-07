from flask import Blueprint
from flask import request

from controllers.tableController import TableController

table_blueprints = Blueprint('table_controller', __name__)
table_controller = TableController()


@table_blueprints.route("/table/all", methods=['GET'])
def get_all_departments():
    response = table_controller.index()
    return response, 200


@table_blueprints.route("/table/<string:id_>", methods=['GET'])
def get_department_by_id(id_):
    response = table_controller.show(id_)
    return response, 200


@table_blueprints.route("/table/insert", methods=['POST'])
def insert_department():
    table = request.get_json()
    response = table_controller.create(table)
    return response, 201


@table_blueprints.route("/table/update/<string:id_>", methods=['PATCH'])
def update_department(id_):
    table = request.get_json()
    response = table_controller.update(id_, table)
    return response, 201


@table_blueprints.route("/table/delete/<string:id_>", methods=['DELETE'])
def delete_department(id_):
    response = table_controller.delete(id_)
    return response, 204

