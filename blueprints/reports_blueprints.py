from flask import Blueprint
from controllers.reports_controller import ReportController


report_blueprints = Blueprint('report_blueprints', __name__)
report_controller = ReportController()


@report_blueprints.route("/reports/highest_votes_candidate", methods=['GET'])
def get_highest_votes_candidate_by_table():
    response = report_controller.get_greatest_votes_candidate_by_table()
    return response, 200


@report_blueprints.route("/reports/votes", methods=['GET'])
def get_total_votes_candidates():
    response = report_controller.get_total_votes_candidates()
    return response, 200


