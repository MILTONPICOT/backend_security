from models.table import Table


class TableController:
    def __int__(self):
        print("Table controller ready...")

    # Get all
    def index(self):
        """

        :return:
        """

        print("Get all")
        data = {
            "_id": "1",
            "numero_mesa": "12",
            "cantidad_CC_inscritas": "231"
        }
        return [data]

    # Get id
    def Show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        data = {
            "_id": "id_",
            "numero_mesa": "8",
            "cantidad_CC_inscritas": "231"
        }
        return data

    # Insert table
    def Create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("Insert")
        table = Table(table_)
        return table.__dict__

    # Update table
    def Update(self, id_: str, table_:dict) -> dict:
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

    # Delete table
    def Delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete"+ id_)
        return {"delete" :1}