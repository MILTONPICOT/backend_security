class CandidateController():
    # Constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("Table controller ready...")

    # Get all candidates
    def index(self) -> list:
        """
        This method get all the candidates into the DB

        :return: candidate's List
        """
        print("Get all")

    # Get Ome candidate by ID
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")

    # INSERT candidate
    def create(self, candidate_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("Insert")

    # UPDATE candidate
    def update(self, id_: str, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("Update")

    # DELETE candidate
    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete Candidate")
