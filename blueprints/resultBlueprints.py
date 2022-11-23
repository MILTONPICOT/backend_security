from flask import Blueprint
from flask import request

from controllers.resultController import ResultController

result_blueprints = Blueprint('result_blueprints', __name__)
result_controller = ResultController()


@result_blueprints.route("/result/all", methods=['GET'])
def get_all_result():
    response = result_controller.index()
    return response, 200


@result_blueprints.route("/result/<string:id_>", methods=['GET'])
def get_result_by_id(id_):
    response = result_controller.show(id_)
    return response, 200


@result_blueprints.route("/result/insert/candidate/<string:candidate_id>/table/<string:table_id>", methods=['POST'])
def insert_result(candidate_id, table_id):
    enrollment = request.get_json()
    response = result_controller.create(enrollment, candidate_id, table_id)
    return response, 201


@result_blueprints.route("/result/update/<string:id_>", methods=['PATCH'])
def update_result(id_):
    enrollment = request.get_json()
    response = result_controller.update(id_, enrollment)
    return response, 201


@result_blueprints.route("/result/delete/<string:id_>", methods=['DELETE'])
def delete_result(id_):
    response = result_controller.delete(id_)
    return response, 204

