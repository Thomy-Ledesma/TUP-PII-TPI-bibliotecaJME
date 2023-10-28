from datetime import *

class Archivo:
    def __init__(self, nombre: str, fecha: date, formato: str):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__formato = formato
        
    @property
    def nombre(self):
        return self.__nombre
    
    property
    def fecha(self):
        return self.__fecha.strftime("%d/%m/%Y")
    
    property
    def formato(self):
        return self.__formato  
        
        
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} - Fecha: {self.__fecha} - Formato: {self.__formato}"