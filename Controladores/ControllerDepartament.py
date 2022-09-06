from Repositorio.RepositorioDepartament import RepositorioDepartament
from Modelos.Departament import Departament

class ControllerDepartament():
    def __init__(self):
        self.repositorioDepartamento = RepositorioDepartament()
    def index(self):
        return self.repositorioDepartamento.findAll()
    def create(self,infoDepartamento):
        nuevoDepartamento=Departament(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)
    def show(self,id):
        elDepartamento=Departament(self.repositorioDepartamento.findById(id))
        return elDepartamento.__dict__
    
    def update(self,id,infoDepartamento):
        DepartamentoActual=Departament(self.repositorioDepartamento.findById(id))
        DepartamentoActual.nombre=infoDepartamento["nombre"]
        DepartamentoActual.descripcion = infoDepartamento["descripcion"]
        return self.repositorioDepartamento.save(DepartamentoActual)
    def delete(self,id):
        return self.repositorioDepartamento.delete(id)