from flask import Blueprint
from controllers.reports_controller import ReportController

reports_blueprints = Blueprint('report_controller', __name__)
report_controller = ReportController()


@reports_blueprints.route("/reports/highest_votes", methods=['GET'])
def get_highest_votes():
    response = report_controller.get_greatest_votes()
    return response, 200


@reports_blueprints.route("/reports/result_by_table", methods=['GET'])
def get_result_by_table():
    response = report_controller.get_result_by_table()
    return response, 200


@reports_blueprints.route("/reports/result_by_candidate", methods=['GET'])
def get_result_by_candidate():
    response = report_controller.get_result_by_candidate()
    return response, 200


@reports_blueprints.route("/reports/result_by_politicalparty", methods=['GET'])
def get_result_by_politicalparty():
    response = report_controller.get_result_by_politicalparty()
    return response, 200


