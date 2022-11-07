from models.table import Table
from repositories.table_repository import TableRepository


class TableController():
    # Constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("Table controller ready...")
        self.table_repository = TableRepository()

    # Get all tables
    def index(self) -> list:
        """
        This method get all  the tables into the DB

        :return: student's List
        """
        return self.table_repository.find_all()

    # Get Ome table by ID
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.table_repository.find_by_id(id_)

    # INSERT table

    def create(self, table_: dict) -> dict:

        """

        :param table_:
        :return:
        """
        print("Insert")
        table = Table(table_)
        return self.table_repository.save(table)


    # UPDATE table
    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update")
        table = Table(table_)
        return self.table_repository.update(id_, table)

    # DELETE table
    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete" + id_)
        return self.table_repository.delete(id_)



