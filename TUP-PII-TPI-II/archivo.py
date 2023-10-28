from datetime import datetime

class Archivo:
    def __init__(self, nombre: str, formato: str):
        self.__nombre = nombre
        self.__fecha = datetime.today().strftime("%d/%m/%Y")
        self.__formato = formato
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def formato(self):
        return self.__formato  
        
        
    def __str__(self) -> str:
        print(f"Nombre: {self.nombre} - Fecha: {self.fecha} - Formato: {self.formato}")