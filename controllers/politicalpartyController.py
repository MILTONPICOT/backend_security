from models.politicalparty import PoliticalParty
from repositories.politicalpartyRepository import PoliticalPartyRepository


class PoliticalPartyController():
    def __init__(self):
        print("Political Party controller ready...")
        self.politicalparty_repository = PoliticalPartyRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("Get all")
        return self.politicalparty_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.politicalparty_repository.find_by_id(id_)

    def create(self, politicalparty_: dict) -> dict:
        """

        :param politicalparty_:
        :return:
        """
        print("Insert")
        politicalparty = PoliticalParty(politicalparty_)
        return self.politicalparty_repository.save(politicalparty)

    def update(self, id_: str, politicalparty_: dict) -> dict:
        """

        :param id_:
        :param politicalparty_:
        :return:
        """
        print("Update")
        politicalparty = PoliticalParty(politicalparty_)
        return self.politicalparty_repository.update(id_, politicalparty)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete")
        return self.politicalparty_repository.delete(id_)
