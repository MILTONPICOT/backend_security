import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient

client = pymongo.MongoClient(
    "mongodb+srv://Mzrbx7:Jod345@mticc4votaciones.ymr6g60.mongodb.net/votaciones_db?retryWrites=true&w=majority",
    tlsCAFile =ca
)
db = client.test
print(db)

data_base = client['votaciones_db']
print(data_base.list_collection_names())