class ResultController:
    def __int__(self):
        print("Results controller ready...")

    # get all
    def index(self):
        print("Get all")

    # Get id
    def show(self, id_: str) -> dict:
        print("Show by id")

    # Insert result
    def create(self, result_:dict) -> dict:
        print("Insert result")

    # Update result
    def Update(self, id_: str, result_:dict)->dict:
        print("Update result")

    # Delete result
    def Delete(self,id_:str) -> str:
        print("Delete")

