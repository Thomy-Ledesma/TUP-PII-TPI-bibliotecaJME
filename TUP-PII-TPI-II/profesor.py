class Profesor():
    def __init__(self, titulo: str, anio_egreso: int):
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso