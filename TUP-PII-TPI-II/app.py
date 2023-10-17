from usuario import *
from estudiante import *
from profesor import *
from curso import *
import os

def ingresar_estudiante(estudiantes):
    
    email = input("Ingrese su email: ")
        
    estudiante_encontrado = None
    for estudiante in estudiantes:
        if estudiante.email == email:
            estudiante_encontrado = estudiante
            break
        
    contrasena = input("Ingrese su contraseña: ")
        
    if estudiante_encontrado != None:
        if estudiante_encontrado.validar_credenciales(email, contrasena):
            print("Acceso concedido. Bienvenido")
            
            respuesta = ""
            def menu():
                print("1.- Matricularse a un curso.")
                print("2.- Ver curso")
                print("3.- Volver al menu principal")
                
            while respuesta != "Salir":
                menu()
                opcion = input("Ingrese una opción del menú: ")
                if opcion.isnumeric():
                    if int(opcion) == 1:
                        nuevo_curso = matricularse_a_un_curso(estudiante_encontrado)
                        if nuevo_curso != None:
                            estudiante_encontrado.cursos.append(nuevo_curso)
                        print(estudiantes[2].cursos)
                    elif int(opcion) == 2:
                        ver_cursos()
                    elif int(opcion) == 3:
                        print("Volviendo al menu principal..")
                        break
                    else:
                        print("Ingrese una opción valida")
                else:
                    print("Ingrese una opción numérica")

                input("Presione cualquier tecla para volver al menú principal")

            print("Hasta luego!")
                
            
        else:
            print("Error de ingreso, vuelva a intentar.")
    else:
        print("Alumno inexistente. Debe darse de alta!")
    
    
def ingresar_profesor(profesores):
    email = input("Ingrese su email: ")
    
    profesor_encontrado = None
    for profesor in profesores:
        if profesor.email == email:
            profesor_encontrado = profesor
            break
    
    contrasena = input("Ingrese su contraseña: ")
    
    if profesor_encontrado != None:
        if profesor_encontrado.validar_credenciales(email, contrasena):
            print("Acceso concedido.")
        else:
            print("Error de ingreso, vuelva a intentar.")
    else:
        print("Alumno inexistente. Debe darse de alta!")
        


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







def matricularse_a_un_curso(alumno):
    return ver_cursos(alumno)



print("Bienvenido, las opciones son: \n")
respuesta = ""

def menu():
    print("1.- Ingresar como estudiante")
    print("2.- Ingresar como profesor")
    print("3.- Ver cursos")
    print("4.- Salir")
    
while respuesta != "Salir":
    menu()
    opcion = input("Ingrese una opción del menú: ")
    if opcion.isnumeric():
        if int(opcion) == 1:
            ingresar_estudiante(estudiantes)
        elif int(opcion) == 2:
            ingresar_profesor()
        elif int(opcion) == 3:
            ver_cursos()
        elif int(opcion) == 4:
            print("Saliendo del sistema..")
            break
        else:
            print("Ingrese una opción valida")
    else:
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para salir")
    
print("Hasta luego!")
    