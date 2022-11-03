

class PoliticalPartyController:
    def __int__(self):
        print("Political party controller ready")

    # Get all
    def index(self):
        print("Get all")

    # Get id
    def show(self, id_: str) -> dict:
        print("Show by id")

    # Insert Political party
    def Create(self, politicalParty_: dict) -> dict:
        print("insert Political Party")

    # Update Polical party
    def Update(self,id_: str, politicalParty_: dict) -> dict:
        print("Update Political Party")

    # Delete Polical party
    def Delete(self, id_: str) -> str:
        print("Delete Political party")
