from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControlerStudent
from Controladores.ControllerCourse import ControllerCourse
from Controladores.ControllerDepartament import ControllerDepartament

app = Flask(__name__)
cors = CORS(app)

myControllerStudent = ControlerStudent()
myControllerCourse = ControllerCourse()
myControlerDepartament = ControllerDepartament()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    json = myControllerStudent.index()
    return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = myControllerStudent.create(data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
    json = myControllerStudent.show(id)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = myControllerStudent.update(id, data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json = myControllerStudent.delete(id)
    return jsonify(json)

# rutas departamento


@app.route("/departamento", methods=['GET'])
def getDepartamentos():
    json = myControlerDepartament.index()
    return jsonify(json)


@app.route("/departamento", methods=['POST'])
def crearDepartamentoe():
    data = request.get_json()
    json = myControlerDepartament.create(data)
    return jsonify(json)


@app.route("/departamento/<string:id>", methods=['GET'])
def getDepartamento(id):
    json = myControlerDepartament.show(id)
    return jsonify(json)


@app.route("/departamento/<string:id>", methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json = myControlerDepartament.update(id, data)
    return jsonify(json)


@app.route("/departamento/<string:id>", methods=['DELETE'])
def eliminarDepartamento(id):
    json = myControlerDepartament.delete(id)
    return jsonify(json)

# Materias


@app.route("/materias", methods=['GET'])
def getMaterias():
    json = myControllerCourse.index()
    return jsonify(json)


@app.route("/materias", methods=['POST'])
def crearMateria():
    data = request.get_json()
    json = myControllerCourse.create(data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['GET'])
def getMateria(id):
    json = myControllerCourse.show(id)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json = myControllerCourse.update(id, data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['DELETE'])
def eliminarMateria(id):
    json = myControllerCourse.delete(id)
    return jsonify(json)


@app.route("/materias/<string:id>/departamento/<string:id_departamento>", methods=['PUT'])
def asignarDepartamentoAMateria(id, id_departamento):
    json = myControllerCourse.asignarDepartamento(id, id_departamento)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" +
          dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
