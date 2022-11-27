from flask import Blueprint
from flask import request

from controller.results_controller import ResultController

result_blueprints = Blueprint('result_blueprints', __name__)
results_controller = ResultController()


@result_blueprints.route("/result/all", methods=['GET'])
def get_all_results():
    response = results_controller.index()
    return response, 200


@result_blueprints.route("/result/<string:id_>", methods=['GET'])
def get_result_by_id(id_):
    response = results_controller.show(id_)
    return response, 200


@result_blueprints.route("/result/candidate/<string:candidate>", methods=['GET'])
def get_result_by_candidate(candidate_id):
    response = results_controller.get_by_candidate(candidate_id)
    return response, 200


@result_blueprints.route("/result/insert/candidate/<string:candidate_id>/table/<string:table_id>", methods=['POST'])
def insert_enrollment(candidate_id, table_id):
    enrollment = request.get_json()
    response = results_controller.create(enrollment, candidate_id, table_id)
    return response, 201


@result_blueprints.route("/result/update/<string:id_>", methods=['PATCH'])
def update_result(id_):
    result = request.get_json()
    response = results_controller.update(id_, result)
    return response, 201


@result_blueprints.route("/result/delete/<string:id_>", methods=['DELETE'])
def delete_result(id_):
    response = results_controller.delete(id_)
    return response, 204
