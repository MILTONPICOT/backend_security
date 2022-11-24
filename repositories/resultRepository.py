from bson import ObjectId

from models.result import Result
from repositories.interface_repository import InterfaceRepository


class ResultRepository(InterfaceRepository[Result]):
    def get_result_in_table(self, table_id: str) -> list:
        """

        :param table_id:
        :return:
        """
        query = {"table.$id": ObjectId(table_id)}
        return self.query(query)
