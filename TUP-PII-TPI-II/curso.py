import string, random
import os

def generar_clave():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod

class Curso:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__clave = generar_clave()
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def clave(self):
        return self.__clave
    
        
materia = Curso("ingles")

print(materia)
    
        

cursos = {
    "Tecnicatura Universitaria en Programación" : ["Ingles II","Ingles I","Laboratiorio I","Laboratiorio II","Programación I","Programación II"],
    "Ingenieria en sistemas" : ["Proximamente... ;)"]
}



def ver_cursos(usuario = None):
    i = 0
    os.system ("cls") #Limpiar pantalla
    carreras_lista = list(cursos.keys())
    for carreras in carreras_lista:
        print(f'\n{i + 1} - {carreras}')
        i += 1
    print("\n")
    carrera = int(input("Seleccione la carrera: "))
    carrera = cursos[carreras_lista[carrera - 1]]
    carrera.sort()
    os.system ("cls") #Limpiar pantalla
    i = 0
    for materias in carrera:
        print(f'{i+1} - {materias} \n')
        i += 1
    if usuario != None:
        curso_inscripcion = input("Seleccione el curso a inscribirse: ")
        if curso_inscripcion.isnumeric():
            if int(curso_inscripcion) in range(1, len(carrera) + 1):
                if(carrera[int(curso_inscripcion) - 1] in usuario.cursos):
                    print("El usuario ya se encuentra en este curso")
                    return None
                return carrera[int(curso_inscripcion) - 1]
            else:
                print("Opción fuera de rango")
        else:
            print("Opción no numerica")


def cursos_inscripto(usuario):
    cursos = usuario.cursos
    if cursos != []:
        for curso in cursos: 
            print(f'- {curso}')