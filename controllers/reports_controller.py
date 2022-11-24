from repositories.reports_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_greatest_votes_candidate_by_table(self):
        return self.report_repository.get_greatest_votes_candidate_by_table()

    def get_total_votes_candidates(self):
        return self.report_repository.get_total_votes_candidates()

