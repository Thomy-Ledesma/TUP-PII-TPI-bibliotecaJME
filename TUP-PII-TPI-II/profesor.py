from usuario import *
from carrera import Carrera

class Profesor(Usuario):
    codigo_admin = "Admin123"

    def __init__(self, nombre: str, apellido: str, email: str, contrasena: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasena)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.carreras = []  # Lista de carreras asociadas al profesor
        self.cursos = []
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
       
    def __str__(self):
        return f" Nombre: {self.__nombre}\n Apellido: {self.__apellido}\n Email: {self.__email}"
    
profesores = []
profe1 = Profesor("Jesica", "Rodriguez", "2", "2", "Ingenieria Quimica", 2015)
profe2 = Profesor("Esteban", "Perez", "estebanperez@gmail.com", "esteban1986", "Ingenieria Electrica", 2009)
profesores.append(profe1)
profesores.append(profe2)