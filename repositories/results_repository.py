from bson import ObjectId

from models.results import Result
from repositories.interface_repository import InterfaceRepository


class ResultRepository(InterfaceRepository[Result]):
    def get_table_in_candidate(self, candidate_id: str):
        query = {"candidate_$id": ObjectId(candidate_id)}
        return self.query(query)

