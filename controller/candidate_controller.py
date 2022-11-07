from repositories.candidate_repository import Candidate_repository
from repositories.politicalParty_Repository import PoliticalParty_repository
from models.candidate import Candidate
from models.politicalParty import PoliticalParty

class Candidate_controller():
    def __init__(self):
        self.repositorioCandidato = Candidate_repository()
        self.repositorioPartido = PoliticalParty_repository()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        nuevoCandidato = Candidate(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self, id):
        elCandidato = Candidate(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        elCandidato = Candidate(self.repositorioCandidato.findById(id))
        elCandidato.cedula = infoCandidato["cedula"]
        elCandidato.numero_resolucion = infoCandidato["numero_resolucion"]
        elCandidato.nombre = infoCandidato["nombre"]
        elCandidato.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(elCandidato)

    def delete(self, id):
        return self.repositorioCandidato.delete(id)
    
    def asignarCandidato(self, id, id_partido):
        candidatoActual = Candidate(self.repositorioCandidato.findById(id))
        partidoActual = PoliticalParty(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)

