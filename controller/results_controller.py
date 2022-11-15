from models.candidate import Candidate
from models.results import Result
from models.table import Table
from repositories.candidate_repository import CandidateRepository
from repositories.results_repository import ResultRepository
from repositories.table_repository import TableRepository


class ResultController:
    def __init__(self):      # Constructor
        print("Results controller ready...")
        self.results_repository = ResultRepository()
        self.candidate_repository = CandidateRepository()
        self.table_repository = TableRepository()

# Get all results
    def index(self) -> list:
        """
        This method get all the results into the DB
        :return: result's List
        """
        return self.results_repository.find_all()

    def show(self, id_: str) -> dict: # Get Ome result by ID
        """
        :param id_:
        :return:
        """
        return self.results_repository.find_by_id(id_)

    def get_by_candidate(self, candidate_id: str) -> list:
        """

        :param candidate_id:
        :return:
        """
        return self.results_repository.get_table_in_candidate(candidate_id)

    def create(self, result_: dict, candidate_id: str, table_id: str) -> dict:
        """

        :param table_id:
        :param candidate_id:
        :param result_:
        :return:
        """
        print("Insert")
        result = Result(result_)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        result.candidate = candidate_obj
        result.table = table_obj
        return self.results_repository.save(result)

    # UPDATE table
    def update(self, id_: str, result_: dict) -> dict:
        """

        :param id_:
        :param result_:
        :return:
        """
        result = Result(result_)
        return self.results_repository.update(id_, result)

    # DELETE table
    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Delete")
        return self.results_repository.delete(id_)
