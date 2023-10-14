from usuario import *

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasena: str, legajo: int, anio_inscripcion_carrera: int):
        super().__init__(nombre, apellido, email, contrasena)
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
          
estudiantes = [
    Estudiante("Ivan", "Porcari", "ivanporcari@gmail.com", "ivan1993", 5050, 2023),
    Estudiante("Jordan", "Pradenas", "jordanpradenas@gmail.com", "jordan1993", 5051, 2023),
    Estudiante("Thomas", "Ledesma", "thomasledesma@gmail.com", "thomas1993", 5052, 2023)
]

#for estudiante in estudiantes:
#    print(f"Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Email: {estudiante.email}, Legajo: {estudiante.legajo}, Año de Inscripción: {estudiante.anio_inscripcion_carrera}")