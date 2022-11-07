#from crypt import methods
from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

from controller.politicalParty_controller import PoliticalParty_controller
from controller.candidate_controller import Candidate_controller
from controller.table_controller import Table_controller
from controller.results_controller import Results_controller

app = Flask(__name__)
cors = CORS(app)


##############################
##     VARIABLES GLOBALES   ##
##############################
miControladorPartido = PoliticalParty_controller()
miControladorCandidato = Candidate_controller()
miControladorMesa = Table_controller()
miControladorResultado = Results_controller()

####################################
##    PROBAR EL SERVICIO          ##
####################################
@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

#####################################
##      ENDPOINT PARTIDOS          ##
#####################################
#OBTENER PARTIDOS
@app.route("/political_Party/all", methods=["GET"])##PROBADO
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)
#CREAR PARTIDO
@app.route("/political_Party/insert", methods=["POST"])#####PROBADO
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)
#MIRAR UN PARTIDO
@app.route("/political_Party/find/<string:id>", methods=["GET"])###PROBADO
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)
#ACTUALIZAR PARTIDO
@app.route("/political_Party/update/<string:id>", methods=["PUT"])##PROBADO
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)
#ELIMINAR PARTIDO
@app.route("/political_Party/delete/<string:id>", methods=["DELETE"])##PROBADO
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

#####################################
##      ENDPOINT CANDIDATOS        ##
#####################################
@app.route("/candidate/all", methods = ["GET"])#PROBADO
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidate/insert", methods =["POST"])#PROBADO
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidate/find/<string:id_candidato>", methods = ["GET"])#PROBADO
def getCandidato(id_candidato):
    json = miControladorCandidato.show(id_candidato)
    return jsonify(json)

@app.route("/candidate/update/<string:id_candidato>", methods = ["PUT"])#PROBADO
def modificarCandidato(id_candidato):
    data = request.get_json()
    json = miControladorCandidato.update(id_candidato, data)
    return jsonify(json)

@app.route("/candidate/delete/<string:id_candidato>", methods = ["DELETE"])#PROBADO
def eliminarCandidato(id_candidato):
    json = miControladorCandidato.delete(id_candidato)
    return jsonify(json)

@app.route("/candidate/<string:id_candidato>/politicalParty/<string:id_partido>", methods=["PUT"])#PROBADO
def asignarPartidoCandidato(id_candidato, id_partido):
    json = miControladorCandidato.asignarCandidato(id_candidato, id_partido)
    return jsonify(json)

#####################################
##           ENDPOINT MESAS        ##
#####################################

@app.route("/table/all", methods=["GET"])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/table/insert", methods=["POST"])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/table/find/<string:id>", methods=["GET"])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/table/update/<string:id>", methods=["PUT"])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/table/delete/<string:id>", methods=["DELETE"])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)




if __name__ == "__main__":
    app.run(debug=False, port=9000)