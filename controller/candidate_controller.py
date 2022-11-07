from models.candidate import Candidate


class CandidateController:
    def __init__(self):
        print("Candidate controller ready...")

    # Get all
    def index(self):
        print("Get all")
        data = {
            "cedula": "123344",
            "nombre": "Juan",
            "apellido": "Rios",
            "id partido": "5"
        }
        return [data]

    # Get id
    def Show(self, id_: str) -> dict:
        print("Show by id")
        data = {
            "cedula": "id_",
            "nombre": "Pedro",
            "apellido": "Paramo",
            "id partido": "6"
        }
        return data

    # Insert Candidate
    def Create(self, candidate_: dict) -> dict:
        print("Insert Candidate")
        candidate = Candidate(candidate_)
        return candidate.__dict__

    # Update Candidate
    def Update(self, id_: str, candidate_: dict) -> dict:
        print("Update candidate")
        data = candidate_
        data['cedula']= id_
        candidate = Candidate(candidate_)
        return candidate.__dict__

    # Delete Candidate
    def Delete(self, id_: str) -> str:
        print("Delete Candidate" + id_)
        return {"delete " :1}
