from estudiante import *
from profesor import *

class Usuario(Estudiante, Profesor): #super clase, recibirá como herencia Estudiante y Profesor
    def __init__(self, nombre: str, apellido: str, email: str, contrasena: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def contrasena(self):
        return self.__contrasena
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
        
    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        self.__apellido = nuevo_apellido
           
    @email.setter #SETTER
    def email(self, nuevo_email: str):
        self.__email = nuevo_email
        
    @contrasena.setter
    def apellido(self, nueva_contrasena: str):
        self.__contrasena = nueva_contrasena
        
    def validar_credenciales(self, email: str, contrasena: str) -> bool:
        if self.__email == email and self.__contrasena == contrasena:
            return True
        return False
    
estudiantes = [
    Estudiante("Ivan", "Porcari", "ivanporcari@gmail.com", "ivan1993", "5050", "2023"),
    Estudiante("Jordan", "Pradenas", "jordanpradenas@gmail.com", "jordan1993", "5051", "2023"),
    Estudiante("Thomas", "Ledesma", "thomasledesma@gmail.com", "thomas1993", "5052", "2023")
]

profesores = [
    Profesor("Jesica", "Rodriguez", "jesicarodriguez@gmail.com", "jesica1986", "Ingenieria Quimica", "2015"),
    Profesor("Esteban", "Perez", "estebanperez@gmail.com", "esteban1986", "Ingenieria Electrica", "2009")
]

carreras = ["Tecnicatura en Programacion"]
