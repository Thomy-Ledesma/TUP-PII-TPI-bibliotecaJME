from curso import *
class Carrera:
    def __init__(self, nombre: str, cant_anios: int = 0):
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__cursos = []

    @property
    def cursos(self):
      return self.__cursos
        
    def agregar_curso(self, curso):
        self.__cursos.append(curso)
        
    def get_cursos(self):
        return self.__cursos  # Método getter para obtener la lista de cursos
        
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} - Cantidad de años: {self.__cant_anios}"
    
    @property
    def nombre(self):
        return self.__nombre
    
    
carrera1 = Carrera("Tecnicatura en programación", 2)
carrera1.agregar_curso(curso1)
carrera1.agregar_curso(curso2)
carrera1.agregar_curso(curso3)
carrera1.agregar_curso(curso4)

carreras = []
carreras.append(carrera1)
