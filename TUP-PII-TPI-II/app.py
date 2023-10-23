from usuario import *
from estudiante import *
from profesor import *
from curso import *

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
                print(f"2.- Ver cursos a los que {estudiante_encontrado.nombre} está inscripto")
                print("3.- Volver al menu principal")
                
            while respuesta != "Salir":
                menu()
                opcion = input("Ingrese una opción del menú: ")
                if opcion.isnumeric():
                    if int(opcion) == 1:
                        matricularse_a_un_curso(estudiante_encontrado)
                    elif int(opcion) == 2:
                        cursos_inscripto(estudiante_encontrado)
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
            print("Acceso concedido. Bienvenido")
            
            respuesta = ""
            def menu():
                print("1.- Dictar Curso.")
                print(f"2.- Ver cursos que {profesor_encontrado.nombre} está dictando")
                print("3.- Volver al menu principal")
                
            while respuesta != "Salir":
                menu()
                opcion = input("Ingrese una opción del menú: ")
                if opcion.isnumeric():
                    if int(opcion) == 1:
                        dictar_un_curso(profesor_encontrado)
                    elif int(opcion) == 2:
                        cursos_dictados(profesor_encontrado)
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
        


def matricularse_a_un_curso(estudiante_encontrado):
    ordenar_cursos = sorted(cursos_lista, key=lambda cursos: cursos.nombre)
    ver_cursos(cursos_lista)
    opcion = input("Seleccione el numero del curso al que se desea matricular: ")
    if opcion.isdigit():
        menu_curso = int(opcion) -1
        if 0 <= menu_curso <len(ordenar_cursos):
            curso = ordenar_cursos[menu_curso]
            clave_matriculacion = input(f"Ingrese la contraseña para matricularse al curso {curso.nombre}: ")
            validar = estudiante_encontrado.validar_clave(curso, clave_matriculacion)
            print(validar)
        else:
            print("Opción no valida, Por favor ingrese una opción que se encuentre en la lista.")
    else:
        print("Opción  invalida, Por favor ingrese una opción que sea numerica.")

def ver_cursos(cursos_lista):
    print("\n Lista de Cursos Disponibles")
    if cursos_lista is not None:
        ordenar_cursos = sorted(cursos_lista, key=lambda cursos: cursos.nombre)
        for i, curso in enumerate(ordenar_cursos, start=1):
            print(f"{i}.-", curso)


def cursos_inscripto(estudiante_encontrado):
    if not estudiante_encontrado.cursos:
        print("Aun no te encuentras matriculado en un curso.")
    else:
        print("\n Cursos en los que estas matriculado.")
        for i, curso in enumerate(estudiante_encontrado.cursos, start=1):
            print(f"{i}. {curso.nombre}")

def dictar_un_curso(profesor_econtrado):
    curso_nombre = input("Ingrese el nombre del curso que va a dictar: ").capitalize()
    for curso in cursos_lista:
        if curso.nombre == curso_nombre:
            print(f"El curso {curso_nombre} ya existe en la lista, por favor ingrese otro")
            return
    clave_matriculacion = Curso.generar_clave()
    curso = Curso(curso_nombre, clave_matriculacion)
    cursos_lista.append(curso)
    profesor_econtrado.cursos.append(curso)
    print(f"Curso ingresado con exito!, \nCurso: {curso_nombre}\nClave Matriculacion: {clave_matriculacion}")
    
def cursos_dictados(profesor_encontrado):
    if not profesor_encontrado.cursos:
        print("Aun no tienes registrado un curso para dictar.")
    else:
        print("Cursos inscriptos para dictar.")
        for i, curso in enumerate(profesor_encontrado.cursos, start=1):
            print(f"{i}.- {curso.nombre} \nClave Matriculacion: {curso.clave}")

#MENU APP 
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
            ingresar_profesor(profesores)
        elif int(opcion) == 3:
            ver_cursos(cursos_lista)
        elif int(opcion) == 4:
            print("Saliendo del sistema..")
            break
        else:
            print("Ingrese una opción valida")
    else:
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para salir")
    
print("Hasta luego!")
    