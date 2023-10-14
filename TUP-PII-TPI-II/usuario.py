class Usuario(): #super clase, Estudiante y Profesor heredarán Usuario
    def __init__(self, nombre: str, apellido: str, email: str, contrasena: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def contrasena(self):
        return self.__contrasena
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
        
    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        self.__apellido = nuevo_apellido
           
    @email.setter #SETTER
    def email(self, nuevo_email: str):
        self.__email = nuevo_email
        
    @contrasena.setter
    def contrasena(self, nueva_contrasena: str):
        self.__contrasena = nueva_contrasena
        
        
    def __str__(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Email: {self.__email}"
        
    def validar_credenciales(self, email: str, contrasena: str) -> bool:
        if self.__email == email and self.__contrasena == contrasena:
            return True
        return False



carreras = ["Tecnicatura en Programacion"]
