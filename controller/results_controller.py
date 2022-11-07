from models.results import Result


class ResultController:
    def __init__(self):
        print("Results controller ready...")

    # get all
    def index(self) -> list:
        print("Get all")
        data = {
            "_id": "1",
            "numero mesa": "2",
            "Id partido": "1"
        }
        return [data]

    # Get id
    def show(self, id_: str) -> dict:
        print("Show by id")
        data = {
            "_id": "id_",
            "numero mesa": "8",
            "Id partido": "6"
        }

    # Insert result
    def create(self, result_:dict) -> dict:
        print("Insert result")
        result = Result(result_)
        return result.__dict__

    # Update result
    def Update(self, id_: str, result_:dict)->dict:
        print("Update result")
        data = result_
        data['_id'] =  id_
        result = Result(result_)
        return result.__dict__

    # Delete result
    def Delete(self,id_:str) -> str:
        print("Delete "+id_)
        return {"delete ": 1}

