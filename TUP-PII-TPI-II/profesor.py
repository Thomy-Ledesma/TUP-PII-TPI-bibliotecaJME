from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasena: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasena)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
       
    def __str__(self):
        return f" Nombre: {self.__nombre}\n Apellido: {self.__apellido}\n Email: {self.__email}"
    
profesores = [
    Profesor("Jesica", "Rodriguez", "jesicarodriguez@gmail.com", "jesica1986", "Ingenieria Quimica", 2015),
    Profesor("Esteban", "Perez", "estebanperez@gmail.com", "esteban1986", "Ingenieria Electrica", 2009)
 ]

#for profesor in profesores:
#    print(f"Nombre: {profesor.nombre}, Apellido: {profesor.apellido}, Email: {profesor.email}, Titulo: {profesor.titulo}, Año de egreso: {profesor.anio_egreso}")