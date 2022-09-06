from Modelos.Student import Student
from Repositorio.RepositorioEstudiante import RepositorioEstudiante

class ControlerStudent():
    def __init__(self):
        print('Creando ControladorStudent')
        self.repositorioEstudiante = RepositorioEstudiante()

    #Funcion que trae la lista de todos los estudiantes con sus atributos
    def index(self):
        print("Listar todos los estudiantes")
        # unEstudiante={
        #     "_id": "abc123",
        #    "cedula": "123",
        #    "nombre":"Yef",
        #    "apellido":"Peña"
        #}

        return self.repositorioEstudiante.findAll()
    #Funcion para crear un objeto de estudiante
    def create(self,infoEstudante):
        print("Crear un estudiante")
        elEstudiante = Student(infoEstudante)
        nuevoEstudiante= Student(infoEstudante)
        return self.repositorioEstudiante.save(nuevoEstudiante)
    #Funcion para mostrar un objeto según su identificador
    def show(self,id):
        print("Mostrando un estudiante con id", id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Yef",
            "apellido": "Peña"
        }
        elEstudiante= Student(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__
    #Funcion para actualizar la informacion de un estudiante
    def update(self, id, infoEstudiante):
        estudianteActual=Student(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula=infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)
    def delete(self, id):
        return self.repositorioEstudiante.delete(id)