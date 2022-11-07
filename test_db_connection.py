import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://mateob:Mateo1014@misionticg10.aslwwzd.mongodb.net/votes_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)

db = client.test
print(db)

data_base = client['votes_db']
print(data_base.list_collection_names())

candidate = data_base.get_collection('candidate')
# all_candidates = candidate.insert
