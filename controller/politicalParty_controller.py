class PoliticalPartyController():
    # Constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("PoliticalParty controller ready...")

    # Get all PoliticalParty
    def index(self) -> list:
        """
        This method get all  the PoliticalParty into the DB

        :return: PoliticalParty List
        """
        print("Get all")

    # Get Ome PoliticalParty by ID
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")

    # INSERT PoliticalParty
    def create(self, PoliticalParty_: dict) -> dict:
        """

        :param PoliticalParty_:
        :return:
        """
        print("Insert")

    # UPDATE PoliticalParty
    def update(self, id_: str, PoliticalParty_: dict) -> dict:
        """

        :param id_:
        :param PoliticalParty_:
        :return:
        """
        print("Update")

    # DELETE PoliticalParty
    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete PoliticalParty")
