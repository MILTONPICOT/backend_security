from models.politicalParty import PoliticalParty


class PoliticalPartyController:
    def __init__(self):
        print("Political party controller ready")

    # Get all
    def index(self)-> list:
        print("Get all")
        data = {
            "_id": "1",
            "nombre": "Amarillo",
            "lema": "Sol"
        }
        return [data]

    # Get id
    def show(self, id_: str) -> dict:
        print("Show by id")
        data = {
            "_id": "id_",
            "nombre": "Azul",
            "lema": "Hoy"
        }
        return data

    # Insert Political party
    def Create(self, politicalParty_: dict) -> dict:
        print("insert Political Party")
        politicalParty = PoliticalParty(PoliticalParty)
        return politicalParty.__dict__

    # Update Polical party
    def Update(self,id_: str, politicalParty_: dict) -> dict:
        print("Update Political Party")
        data = politicalParty_
        data['_id'] = id_
        politicalParty = PoliticalParty(PoliticalParty)
        return politicalParty.__dict__

    # Delete Polical party
    def Delete(self, id_: str) -> str:
        print("Delete Political party " + id_)
        return {"delete ": 1}

