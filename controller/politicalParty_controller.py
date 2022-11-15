from models.politicalParty import PoliticalParty
from repositories.politicalParty_repository import PoliticalPartyRepository


class PoliticalPartyController:
    # Constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("PoliticalParty controller ready...")
        self.politicalParty_repository = PoliticalPartyRepository()

    # Get all PoliticalParty
    def index(self) -> list:
        """
        This method get all  the PoliticalParty into the DB

        :return: PoliticalParty List
        """
        return self.politicalParty_repository.find_all()

    # Get Ome PoliticalParty by ID
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.politicalParty_repository.find_by_id(id_)

    # INSERT PoliticalParty
    def create(self, PoliticalParty_: dict) -> dict:

        """

        :param PoliticalParty_:
        :return:
        """
        print("Insert")
        political_party = PoliticalParty(PoliticalParty_)
        return self.politicalParty_repository.save(political_party)

    # UPDATE PoliticalParty

    def update(self, id_: str, PoliticalParty_: dict) -> dict:
        """

        :param id_:
        :param PoliticalParty_:
        :return:
        """
        print("Update")
        political_party = PoliticalParty(PoliticalParty_)
        return self.politicalParty_repository.update(id_, political_party)

    # DELETE PoliticalParty
    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Delete PoliticalParty")
        return self.politicalParty_repository.delete(id_)
