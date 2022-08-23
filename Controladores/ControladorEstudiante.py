from Modelos.Student import Student

class ControlerStudent():
    def __init__(self):
        print('Creando ControladorStudent')

    #Funcion que trae la lista de todos los estudiantes con sus atributos
    def index(self):
        print("Listar todos los estudiantes")
        unEstudiante={
            "_id": "abc123",
            "cedula": "123",
            "nombre":"Yef",
            "apellido":"Peña"
        }
        return [unEstudiante]
    #Funcion para crear un objeto de estudiante
    def create(self,infoEstudante):
        print("Crear un estudiante")
        elEstudiante = Student(infoEstudante)
        return elEstudiante.__dict__
    #Funcion para mostrar un objeto según su identificador
    def show(self,id):
        print("Mostrando un estudiante con id", id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Yef",
            "apellido": "Peña"
        }
        return elEstudiante
    #Funcion para actualizar la informacion de un estudiante
    def update(self,id,infoEstudiante):
        print("Actualizando estudiante con el id",id)
        elEstudiante=Student(infoEstudiante)
        return elEstudiante.__dict__
    def delete(self,id):
        print("Eliminando con el id")
        return {"deleted_cont":1}