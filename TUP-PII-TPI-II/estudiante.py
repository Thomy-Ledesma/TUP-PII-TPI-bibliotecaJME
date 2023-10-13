

class Estudiante():
    def __init__(self, legajo: int, anio_inscripcion_carrera: int):
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        
    @property
    def legajo(self):
        return self.__legajo
    
    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    def matricular_en_curso():
        pass