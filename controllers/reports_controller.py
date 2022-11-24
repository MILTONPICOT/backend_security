from repositories.reports_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_greatest_votes(self):
        return self.report_repository.get_greatest_votes()

    def get_result_by_table(self):
        return self.report_repository.get_result_by_table()

    def get_result_by_candidate(self):
        return self.report_repository.get_result_by_candidate()


