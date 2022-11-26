from models.result import Result
from repositories.interface_repository import InterfaceRepository


class ReportRepository(InterfaceRepository[Result]):
    def get_greatest_votes(self):
        query_aggregation = {
            "$group": {
                "_id": "$table",
                "max": {
                    "$max": "$candidate"
                },
                "doc": {
                    "$first": "$$ROOt"
                }
            }
        }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_result_by_table(self):
        query_lookup = {
            "$lookup": {
                    "from": "table",
                    "localField": "table.$id",
                    "foreignField": "_id",
                    "as": "details"
            }
        }
        query_unwind = {
            "$unwind": "$details"
        }
        query_group = {
            "$group": {
                "_id": "$details",
                "count": {"$sum": 1}
            }
        }
        query_add_fields = {
            "$addFields":{
                "cedulas_inscritas": "$_id.cedulas_inscritas",
                "numero_de_mesa": "$_id.numero_de_mesa",
                "_id": "$_id._id"
            }
        }
        query_sort = {
            "$sort": {
                "count": -1
            }
        }
        pipeline = [query_lookup, query_unwind, query_group, query_add_fields, query_sort]
        return self.query_aggregation(pipeline)

    def get_result_by_candidate(self):
        query_lookup = {
            "$lookup": {
                  "from": "candidate",
                  "localField": "candidate.$id",
                  "foreignField": "_id",
                  "as": "details"
            }
        }
        query_unwind = {
            "$unwind": "$details"
        }
        query_group = {
            "$group":{
                    "_id": "$details",
                    "count": {"$sum": 1}
            }
        }
        query_add_fields = {
            "$addFields": {
                "numero_resolucion": "$_id.numero_resolucion",
                "nombre": "$_id.nombre",
                "apellido": "$_id.apellido",
                "politicalparty": "$_id.politicalparty",
                "_id": "$_id._id"
            }
        }
        query_sort = {
            "$sort": {
                "count": -1
            }
        }
        pipeline = [query_lookup, query_unwind, query_group, query_add_fields, query_sort]
        return self.query_aggregation(pipeline)
    
        def get_result_by_politicalparty(self):
        query_lookup1 = {
            "$lookup": {
                "from": "candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "candidate_info"
            }
        }
        query_unwind1 = {
            "$unwind": "$candidate_info"
        }
        query_group1 = {
            "$group": {
                "_id": "$candidate_info",
                "count": {"$sum": 1}
            }
        }
        query_add_fields1 = {
            "$addFields": {
                "politicalparty": "$_id.politicalparty"
            }
        }
        query_lookup2 = {
            "$lookup": {
                "from": "politicalparty",
                "localField": "politicalparty.$id",
                "foreignField": "_id",
                "as": "politicalparty_info"
            }
        }
        query_unwind2 = {
            "$unwind": "$politicalparty_info"
        }
        query_group2 = {
            "$group": {
                "_id": "$politicalparty_info",
                "count": {"$sum": "$count"}
            }
        }
        query_add_fields2 = {
            "$addFields": {
                "nombre": "$_id.nombre",
                "id": "$_id._id"
            }
        }
        pipeline = [query_lookup1, query_unwind1, query_group1, query_add_fields1,query_lookup2, query_unwind2,
                    query_group2, query_add_fields2]
        return self.query_aggregation(pipeline)

