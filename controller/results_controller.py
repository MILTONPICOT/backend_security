class ResultController():
    #Constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("Results controller ready...")

# Get all results
    def index(self) -> list:
        """
        This method get all the results into the DB

        :return: result's List
        """
        print("Get all")

    # Get Ome result by ID
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")

    # INSERT table
    def create(self, result_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("Insert")

    # UPDATE table
    def update(self, id_: str, result_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update")

    # DELETE table
    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete")

