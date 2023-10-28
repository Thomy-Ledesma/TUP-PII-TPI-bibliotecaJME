from usuario import *
from archivo import *
import string
import random

class Curso:
    __codigo = 0
    
    def __init__(self, prox_cod: int, nombre: str, codigo :int, clave: str) -> None:
        self.__prox_cod = prox_cod
        self.__nombre = nombre
        self.__codigo = Curso.get_nro_codigo()
        self.__clave = clave
        self.__archivo = archivo
    
    @property
    def prox_cod(self):
        return self.__prox_cod    
        
    @property
    def nombre(self):
        return self.__nombre
    
    @classmethod
    def get_nro_codigo(cls):
        Curso.__codigo += 1
        return Curso.__codigo  
    
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
        
    def nuervo_archivo():
        pass

curso1 = Curso("Laboratorio de Computacion", "111")
curso2 = Curso("Ingles", "222")
curso3 = Curso("Arquitectura de las Computadoras", "333")
curso4 = Curso("Programacion", "444")

cursos_lista =[curso1, curso2, curso3, curso4]
