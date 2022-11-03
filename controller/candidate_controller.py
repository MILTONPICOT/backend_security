

class CandidateController:
    def __int__(self):
        print("Candidate controller ready...")

    # Get all
    def index(self):
        print("Get all")

    # Get id
    def Show(self, id_: str) -> dict:
        print("Show by id")

    # Insert Candidate
    def Create(self, candidate_: dict) -> dict:
        print("Insert Candidate")

    # Update Candidate
    def Update(self, id_: str, candidate_: dict) -> dict:
        print("Update candidate")

    # Delete Candidate
    def Delete(self, id_: str) -> str:
        print("Delete Candidate")
