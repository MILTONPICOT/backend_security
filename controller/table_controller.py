from models.table import Table


class TableController():
    # Constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("Table controller ready...")

    # Get all tables
    def index(self) -> list:
        """
        This method get all  the tables into the DB

        :return: student's List
        """
        print("Get all")
        data = {
            "_id": "abc123",
            "number_table": "12",
            "number_cc_registered": "20"
        }
        return [data]

    # Get Ome table by ID
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        data = {
            "_id": id_,
            "number_table": "12",
            "number_cc_registered": "20"
        }
        return data

    # INSERT table

    def create(self, table_: dict) -> dict:

        """

        :param table_:
        :return:
        """
        print("Insert")
        table = Table(table_)
        return table.__dict__


    # UPDATE table
    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update")
        data = table_
        data['_id'] = id_
        table = Table(table_)
        return table.__dict__

    # DELETE table
    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete" + id_)
        return {"delete": 1}



