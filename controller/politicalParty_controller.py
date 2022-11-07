from repositories.politicalParty_Repository import PoliticalParty_repository
from models.politicalParty import PoliticalParty

class PoliticalParty_controller():
    #Constructor
    def __init__(self):
        self.repositorioPartido = PoliticalParty_repository()
    #Devuelve todos los documentos
    def index(self):
        return self.repositorioPartido.findAll()
    #Crea documentos
    def create(self, infoPartido):
        nuevoPartido = PoliticalParty(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    #Muestra un documento
    def show(self, id):
        elPartido = PoliticalParty(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    #Actualiza un documento
    def update(self, id, infoPartido):
        PartidoActual = PoliticalParty(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)
    #Borra un documento
    def delete(self, id):
        return self.repositorioPartido.delete(id)
