from usuario import *
import string
import random

class Curso:
    def __init__(self, nombre: str, clave: str) -> None:
        self.__nombre = nombre
        self.__clave = clave
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def clave(self):
        return self.__clave
    
    def __str__(self) -> str:
        return f"Curso: {self.nombre}"
    
    @staticmethod
    def generar_clave():
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
        
# materia = Curso("ingles")

# print(materia)
    
# materia_1 = Curso("Ingles I")
# materia_2 = Curso("Ingles II")
# materia_3 = Curso("Laboratorio I")
# materia_4 = Curso("Laboratorio II")
# materia_5 = Curso("Programación I")
# materia_6 = Curso("Programación II")

# cursos = {
#     "Tecnicatura Universitaria en Programación" : [materia_1,materia_2,materia_3,materia_4,materia_5,materia_6],
#     "Ingenieria en sistemas" : ["Proximamente... ;)"]
# }

curso1 = Curso("Laboratorio de Computacion", "111")
curso2 = Curso("Ingles", "222")
curso3 = Curso("Arquitectura de las Computadoras", "333")
curso4 = Curso("Programacion", "444")

cursos_lista =[curso1, curso2, curso3, curso4]

#for curso in cursos_lista:
#    print(f"Nombre: {curso.nombre}, Clave: {curso.clave}")