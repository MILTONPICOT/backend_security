import json

import certifi
import pymongo
from typing import Generic, TypeVar, get_args

from bson import ObjectId, DBRef

T = TypeVar('T')


# todo add date validations and errors hadLing
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

    def save(self, item: T) -> T:
        current_collection = self.data_base[self.collection]
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            # update
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item= item.__dict__
            updated_item = {"$set": item}
            current_collection.update_one({'_id': _id}, updated_item)
        else:
            # insert
            _id = current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__

    def update(self,id_: str,item: T) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        item = item.__dict__
        updated_item = {"$set": item}
        document = current_collection.update_one({'_id':_id},updated_item)
        return {"updated_": document.matched_count}

    def delete(self,id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        result = current_collection.delete_one({'_id': _id})
        return {"deleted_count": result.deleted_count}

    # Todo check if this could be  replace  by find_all
    def query(self, query: dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_value_db_ref(document)
            dataset.append(document)
        return dataset

    # Todo add to find with conditional
    def query_aggregation(self, query: dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.aggregate(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_value_db_ref(document)
            dataset.append(document)
        return dataset

    def get_value_db_ref(self, document: dict) -> dict:
        for key in document.key():
            value = document.get(key)
            if isinstance(document.get(key),DBRef):
                collection_ref = self.data_base[document.get(key).collection]
                _id = ObjectId(value.id)
                document_ref = collection_ref.find({'_id':_id})
                document_ref['_id'] = document_ref['-id'].__str__()
                document[key] = document_ref
                document[key] = self.get_value_db_ref(document[key])
            elif isinstance(value,list) and len(document.get(key)) > 0:
                document[key] = self.get_value_db_ref_from_list(value)
            elif isinstance(value, dict):
                document[key] = self.get_value_db_ref(value)
        return document

    def get_value_db_ref_from_list(self, list_: list) -> list:
        pass

    def transform_object_ids(self):
        pass

    def format_list(self):
        pass

    def transform_refs(self):
        pass

    def object_to_db_ref(self):
        pass






