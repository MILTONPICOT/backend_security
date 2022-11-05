import certifi
import pymongo
from typing import Generic, TypeVar


T = TypeVar('T')


class InterfaceRepository(Generic[T]):

    def __int__(self):
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db_connection"),
        )


    def load_file_config(self):
        with open("config.json", "r") as config:
            data = json.load(config)  # lee el contenido de un archivo json y lo guarda como un diccionario phyton
        return data
