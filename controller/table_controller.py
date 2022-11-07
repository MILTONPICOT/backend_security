from repositories.table_repository import Table_repository
from models.table import Table

class Table_controller():
    #Constructor
    def __init__(self):
        self.repositorioMesa = Table_repository()
    #Devuelve todos los documentos
    def index(self):
        return self.repositorioMesa.findAll()
    #Crea documentos
    def create(self, infoMesa):
        nuevaMesa = Table(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)
    #Muestra un documento
    def show(self, id):
        laMesa = Table(self.repositorioMesa.findById(id))
        return laMesa.__dict__
    #Actualiza un documento
    def update(self, id, infoMesa):
        MesaActual = Table(self.repositorioMesa.findById(id))
        MesaActual.numero = infoMesa["numero"]
        MesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(MesaActual)
    #Borra un documento
    def delete(self, id):
        return self.repositorioMesa.delete(id)
