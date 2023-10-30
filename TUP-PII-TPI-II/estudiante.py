from usuario import *
from curso import *

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasena: str, legajo: int, anio_inscripcion_carrera: int):
        super().__init__(nombre, apellido, email, contrasena)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.cursos = []
        
    @property
    def legajo(self):
        return self.__legajo
    
    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
       
    def __str__(self):
        return f" Nombre: {self.nombre}\n Apellido: {self.apellido}\n Email: {self.email}"
    
    def matricular_en_curso(self, curso: Curso, clave_matriculacion: str):
        if clave_matriculacion == curso.clave:
            if curso not in self.cursos:
                self.cursos.append(curso)
                validar = f"Matriculación en el curso {curso.nombre} exitosa!"
            else:
                validar = f"Ya se encuentra matriculado en el curso {curso.nombre}."
        else:
            validar ="Matriculacion fallida. La contraseña ingresada es incorrecta."
        return validar
    
    def desmatricular_curso(self, curso: Curso, clave_matriculacion: str):
        if clave_matriculacion == curso.clave:
            self.cursos.remove(curso)
            validar = f"Desmatriculación en el curso {curso.nombre} exitosa!"
        else:
            validar ="Desmatriculacion fallida. La contraseña ingresada es incorrecta."
        print(validar)
        
        

estudiantes = []
estudiante1 = Estudiante("Ivan", "Porcari", "ivanporcari@gmail.com", "ivan1993", 5050, 2023)
estudiante2 = Estudiante("Jordan", "Pradenas", "jordanpradenas@gmail.com", "jordan1993", 5051, 2023)
estudiante3 = Estudiante("Thomás", "Ledesma", "1", "1", 5052, 2023)

estudiantes.append(estudiante1)
estudiantes.append(estudiante2)
estudiantes.append(estudiante3)