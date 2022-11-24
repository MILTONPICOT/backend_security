from bson import DBRef

from models.table import Table
from models.result import Result
from models.candidate import Candidate
from repositories.tableRepository import TableRepository
from repositories.resultRepository import ResultRepository
from repositories.candidateRepository import CandidateRepository


class ResultController():
    def __init__(self):
        print("Result control ready...")
        self.result_repository = ResultRepository()
        self.table_repository = TableRepository()
        self.candidate_repository = CandidateRepository()

    def index(self) -> list:
        """

        :return:
        """
        return self.result_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.result_repository.find_by_id(id_)

    def get_by_table(self, table_id: str) -> list:
        """

        :param table_id:
        :return:
        """
        return self.result_repository.get_result_in_table(table_id)

    def create(self, result_: dict, candidate_id: str, table_id: str) -> dict:
        """

        :param table_id:
        :param candidate_id:
        :param result_:
        :return:
        """
        result = Result(result_)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        result.candidate = candidate_obj
        result.table = table_obj
        return self.result_repository.save(result)

    def update(self, id_: str, result_: dict) -> dict:
        """

        :param id_:
        :param result_:
        :return:
        """
        result = Result(result_)
        return self.result_repository.update(id_, result)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        return self.result_repository.delete(id_)
