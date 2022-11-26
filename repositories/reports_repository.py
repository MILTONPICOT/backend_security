from models.result import Result
from repositories.interface_repository import InterfaceRepository


class ReportRepository(InterfaceRepository[Result]):
    def get_greatest_votes_candidate_by_table(self):
        query_aggregation = {
            "$group": {
                "_id": "$table",
                "max": {
                    "$max": "$votes"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_total_votes_candidates(self):
        query_aggregation = {
            '$group': {
                '_id': '$candidate',
                'Total': {
                    '$sum': 1
                },
                'Ref': {
                    '$first': '$$ROOT'
                }
            }
        }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_total_votes_candidates(self):
        query_lookup = {
            '$lookup': {
                'from': 'candidate',
                'localField': 'candidate.$id',
                'foreignField': '_id',
                'as': 'details'
            }
        }

        query_unwind = {
            '$unwind': '$details'
        }
        query_group = {
            '$group': {
                '_id': '$details',
                'Total': {
                    '$sum': 1
                }
            }
        }
        query_add_fields = {
            '$addFields': {
                '_id': '$_id._id',
                'name': '$_id.name',
                'lastname': '$_id.lastname',
                'n_reso': '$_id.n_reso'
            }
        }
        query_sort = {
            '$sort': {
                'Total': -1
            }
        }
        pipline = [query_lookup, query_unwind, query_group, query_add_fields, query_sort]
        return self.query_aggregation(pipline)

    def get_total_votes_politicalparty(self):
        query_lookup_candidate = {
            '$lookup': {
                'from': 'candidate',
                'localField': 'candidate.$id',
                'foreignField': '_id',
                'as': 'details'
            }
        }
        query_unwind_candidate = {
            '$unwind': '$details'
        }
        query_lookup_politicalparty = {
            '$lookup': {
                'from': 'politicalparty',
                'localField': 'details.politicalparty.$id',
                'foreignField': '_id',
                'as': 'details_p'
            }
        }
        query_unwind_politicalparty = {
            '$unwind': '$details_p'
        }
        query_group = {
            '$group': {
                '_id': '$details_p',
                'Total': {
                    '$sum': 1
                    }
                }
            }

        query_add_fields = {
            '$addFields': {
                '_id': '$_id._id',
                'name': '$_id.name',
                'motto': '$_id.motto'
            }
        }
        query_sort = {
            '$sort': {
                'Total': -1
            }
        }
        pipline = [query_lookup_candidate, query_unwind_candidate, query_lookup_politicalparty,
                   query_unwind_politicalparty, query_group, query_add_fields, query_sort]
        return self.query_aggregation(pipline)

    def get_votes_table(self):
        query_lookup = {
            '$lookup': {
                'from': 'table',
                'localField': 'table.$id',
                'foreignField': '_id',
                'as': 'details_t'
            }
        }
        query_unwind = {
            '$unwind': '$details_t'
        }
        query_group = {
            '$group': {
                '_id': '$details_t',
                'Total': {
                    '$sum': 1
                }
            }
        }
        query_add_fields = {
            '$addFields': {
                '_id': '$_id._id',
                'n_table': '$_id.n-table'
            }
        }
        pipline = [query_lookup, query_unwind, query_group, query_add_fields]
        return self.query_aggregation(pipline)
    
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


