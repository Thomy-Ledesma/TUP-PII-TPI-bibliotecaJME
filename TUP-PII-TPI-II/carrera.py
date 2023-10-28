class Carrera:
    def __init__(self, nombre: str, cant_anios: int):
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        
        
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} - Cantidad de años: {self.__cant_anios}"