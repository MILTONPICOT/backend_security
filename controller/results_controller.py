from repositories.results_repository import Results_repository
from repositories.table_repository import Table_repository
from repositories.candidate_repository import Candidate_repository

from models.results import Results
from models.candidate import Candidate
from models.table import Table

class Results_controller():
    def __init__(self):
        self.repositorioResultado = Results_repository()
        self.repositorioCandidato = Candidate_repository()
        self.repositorioMesa = Table_repository()

    def index(self): 
        return self.repositorioResultado.findAll()

    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Results(infoResultado)
        laMesa = Table(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidate(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Results(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultado, id_mesa, id_candidato):
        elResultado = Results(self.repositorioResultado.findById(id))
        laMesa = Table(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidate(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    def getListarCandidatosMesa(self, id_mesa):
        return self.repositorioResultado.getListadoCandidatosInscritosMesa(id_mesa)

    def getListarMesasDeInscritoCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoMesasCandidatoInscrito(id_candidato)

    def getMayorCedula(self):
        return self.repositorioResultado.getNumeroCedulaMayorCandidato()