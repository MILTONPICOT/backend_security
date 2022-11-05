import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://picot:mcpm8021216@misiontic2022g1.vwmnjij.mongodb.net/votaciones_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)

db = client.test
print(db)

data_base = client['votaciones_db']
print(data_base.list_collection_names())

