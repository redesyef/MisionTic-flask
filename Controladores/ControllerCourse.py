
from Repositorio.RepositorioMateria import RepositorioMateria
from Repositorio.RepositorioDepartament import RepositorioDepartament
from Modelos.Course import Course
from Modelos.Departament import Departament

class ControllerCourse():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartament()
    def index(self):
        return self.repositorioMateria.findAll()
    def create(self,infoMateria):
        nuevoMateria=Course(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)
    def show(self,id):
        elMateria=Course(self.repositorioMateria.findById(id))
        return elMateria.__dict__

    def update(self, id, infoMateria):
        materiaActual = Course(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        return self.repositorioMateria.delete(id)

##relación course - departament
    def asignarDepartamento(self, id, id_departamento):
        materiaActual = Course(self.repositorioMateria.findById(id))
        departamentoActual = Departament(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departament = departamentoActual
        return self.repositorioMateria.save(materiaActual)
