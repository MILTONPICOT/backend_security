import json

import certifi
import pymongo
from typing import Generic, TypeVar, get_args

from bson import ObjectId

T = TypeVar('T')


class InterfaceRepository(Generic[T]):

    def __init__(self):
        # connect to database
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db-connection"),
            tlsCAFile=ca
        )
        self.data_base = client[data_config.get("db-name")]
        # get generic class name
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_file_config(self) -> dict:
        with open("config.json", "r") as config:
            data = json.load(config)
        return data

    def find_all(self) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find({}):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_value_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self,id_:str) -> T:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        document = current_collection.find({'_id':_id})
        document = self.get_value_db_ref(document)
        if not document:
            document['_id'] = document['_id'].__str__()
        else:
            # document no found
            document = {}
        return document

    def insert(self,item: T) -> T:
        current_collection = self.data_base[self.collection]
        pass

    def update(self,id_: str,item: T) -> dict:
        current_collection = self.data_base[self.collection]
        pass

    def delete(self,id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        pass

    def query(self,query: dict) -> list:
        pass

    def query_aggregation(self, query: dict) -> list:
        pass

    def get_value_db_ref(self):
        pass

    def get_value_db_ref_from_list(self):
        pass

    def transform_object_ids(self):
        pass

    def transform_refs(self):
        pass

    def format_list(self):
        pass

    def object_to_db_ref(self):
        pass






