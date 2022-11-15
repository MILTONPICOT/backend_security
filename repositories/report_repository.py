from models.results import Result
from repositories.interface_repository import InterfaceRepository


class ReportRepository(InterfaceRepository[Result]):
    def get_greatest_grade(self):
        query_aggregation = {
                "_id": "$table",
                "max": {"$max": "total_votos"},
                "doc": {"$first": "$$ROOT"}
            }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)
