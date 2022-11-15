from flask import Blueprint
from controller.reports_controller import ReportController


report_blueprints = Blueprint('report_blueprints', __name__)
report_controller = ReportController()


@report_blueprints.route("/reports/highest_grade", methods=['GET'])
def get_highest_grade():
    response = report_controller.get_greatest_grade()
    return response, 200
