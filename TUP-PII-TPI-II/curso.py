from usuario import *
from archivo import *
import string
import random
    
class Curso:
    _code = 1 #planetamos una variable de clase para aplicar el código a cada instancia
    def __init__(self, nombre: str, clave:str = ""):
        self.__nombre = nombre
        if clave == "":
            self.__clave = Curso.generar_clave()
        else:
            self.__clave = clave
        self.__codigo = Curso._code
        self.__prox_cod = self.__codigo + 1 #la incrementamos dentro de la instancia
        self.__archivos = []
        Curso._code = self.__prox_cod #asignamos la variable incrementada al codigo para que la próxima instancia de la clase tenga el siguiente código (podría haberse hecho de otra forma pero se respetó el diagrama UML)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def clave(self):
        return self.__clave

    @property
    def archivos(self):
        return self.__archivos
    
    @classmethod
    def generar_clave(self):
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        print(f"la contraseña es {cod}")
        return cod

    def __str__(self) -> str:
        return f"Curso: {self.nombre}"

    def nuevo_archivo(self, archivo: Archivo):
        new_archivo = archivo
        self.archivos.append(new_archivo)

    def ver_archivos(self):
        print(f"Archivos de {self.nombre}:")
        for archivo in self.archivos:
            print(f" {archivo.nombre}.{archivo.formato}")


curso1 = Curso("Laboratorio de Computacion", "111")
curso2 = Curso("Ingles", "222")
curso3 = Curso("Arquitectura de las Computadoras", "333")
curso4 = Curso("Programacion", "444")


archivo1 = Archivo("tp1","pdf")
archivo2 = Archivo("tp2","docx")

curso1.nuevo_archivo(archivo1)

curso1.nuevo_archivo(archivo2)


