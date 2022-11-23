from models.candidate import Candidate
from models.politicalparty import PoliticalParty
from repositories.candidateRepository import CandidateRepository
from repositories.politicalpartyRepository import PoliticalPartyRepository


class CandidateController():
    # Constructor
    def __init__(self):
        print("Candidate controller ready...")
        self.candidate_repository = CandidateRepository()
        self.political_party_repository = PoliticalPartyRepository()

    # get ALL Candidates
    def index(self) -> list:
        """

        :param self:
        :return:
        """
        print("Get all")
        return self.candidate_repository.find_all()

    # get ONE Candidate by ID
    def show(self, id_: str) -> dict:
        """

        :param self:
        :param id_:
        :return:
        """
        print("Show by id")
        return self.candidate_repository.find_by_id(id_)

    # INSERT Candidate
    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """
        print("Insert")
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    # UPDATE Candidate
    def update(self, id_: str, candidate_: dict) -> dict:
        """

        :param self:
        :param id_:
        :param candidate_:
        :return:
        """
        print("Update")
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(id_, candidate)
    # DELETE Candidate

    def delete(self, id_: str) -> str:
        """

        :param self:
        :param id_:
        :return:
        """
        print("Delete " + id_)
        return self.candidate_repository.delete(id_)

    def political_party_assign(self, candidate_id: str, political_party_id: str) -> dict:
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        political_party_dict = self.political_party_repository.find_by_id(political_party_id)
        political_party_obj = PoliticalParty(political_party_dict)
        candidate_obj.politicalparty = political_party_obj
        return self.candidate_repository.save(candidate_obj)
