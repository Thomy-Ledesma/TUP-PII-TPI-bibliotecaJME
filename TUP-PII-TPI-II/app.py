from usuario import *
from estudiante import *
from profesor import *
from curso import *
from carrera import *


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
            print(f"Acceso concedido. Bienvenido {estudiante_encontrado.nombre}")
            
            respuesta = ""
            def menu():
                print("1 - Matricularse a un curso.")
                print("2 - Desmatricularse de un curso.")
                print("3 - Ver cursos inscriptos")
                print("4 - Volver al menu principal")
                
            while respuesta != "Salir":
                menu()
                opcion = input("Ingrese una opción del menú: ")
                if opcion.isnumeric():
                    if int(opcion) == 1:
                        matricularse_a_un_curso(estudiante_encontrado)
                    elif int(opcion) ==2:
                        cursos_inscripto(estudiante_encontrado, True)
                    elif int(opcion) == 3:
                        cursos_inscripto(estudiante_encontrado)
                    elif int(opcion) == 4:
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

def registrar_profesor():
    profe_nombre = input("ingrese el nombre: ")
    profe_apellido = input("ingrese el apellido: ")
    profe_mail = input("ingrese el mail: ")
    profe_password = input("ingrese la contraseña: ")
    profe_titulo = input("ingrese el titulo: ")
    yearprofe = int(input("ingrese el año de egreso: "))
    profesores.append(Profesor(profe_nombre,profe_apellido,profe_mail,profe_password,profe_titulo,yearprofe))   
    
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
                        dictar_un_curso(profesor_encontrado, carreras)
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
        codigo_admin = input("Profesor inexistente. Ingrese el código de Admin para darse de alta: ")
        if codigo_admin == Profesor.codigo_admin:
            registrar_profesor()
        else:
            print("Código incorrecto :(")


def matricularse_a_un_curso(estudiante_encontrado):
    if not carreras:
        print("No hay cursos disponibles. Espere que el profesor lo de alta.")
    else:
        curso_a_inscribir = ver_cursos(carreras)
        #si no hay cursos vuelve al menú principal
        password = input("ingrese la contraseña del curso: ")
        estudiante_encontrado.matricular_en_curso(curso_a_inscribir, password)
        
def ver_cursos(carreras, readonly = False):
    i = 1
    if not carreras:
        print("No hay cursos disponibles. Espere que el profesor lo de alta.")
    else:
        for carrera in carreras:
            print(f"{i} - {carrera.nombre}")
            i += 1
        while True:
            input_carrera = input("Seleccione la carrera: ")
            if input_carrera.isnumeric():
                carrera_seleccionada = int(input_carrera)-1
                if 0 <= carrera_seleccionada <= len(carreras):
                    break
                else:
                    print("Selección inválida. Por favor, elija una opción válida.")
            else:
                print("Selección inválida. Por favor, seleccione un numero.")
        i = 1
        for curso in carreras[int(carrera_seleccionada)].cursos:
            print(f"{i} - {curso.nombre}")
            i += 1
        if not readonly:
            while True:
                input_usuario = input("Ingrese el número del curso al que se desea matricular: ")
                if input_usuario.isnumeric():
                    curso_seleccionado = int(input_usuario) -1
                    if 0 <= curso_seleccionado < len(carreras[carrera_seleccionada].cursos):
                        return carreras[carrera_seleccionada].cursos[curso_seleccionado]
                    else:
                        print("Selección inválida. Por favor, elija una opción válida.")
                else:
                    print("Por favor, ingrese un número válido.")
        

def cursos_inscripto(estudiante_encontrado, desmatricular = False):
    if not estudiante_encontrado.cursos:
        print("Aun no te encuentras matriculado en ningún curso.")
    else:
        print("\n Cursos en los que estas matriculado.")
        for i, curso in enumerate(estudiante_encontrado.cursos, start=1):
            print(f"{i}. {curso.nombre}")
        
        materia = estudiante_encontrado.cursos[int(input("seleccione el curso: ")) - 1]
        
        if desmatricular:
            password = input("ingrese la contraseña del curso: ")
            estudiante_encontrado.desmatricular_curso(materia, password)
        else:
            materia.ver_archivos()


def dictar_un_curso(profesor, carreras):
    i = 0
    # Solicitar al profesor que elija una carrera para el curso
    print("Carreras disponibles:")
    for i, carrera in enumerate(carreras, start=1):
        print(f"{i}.- {carrera.nombre}")
    print(f"{len(carreras) + 1}.- Ingresar nueva carrera")

    while True:
        seleccion_carrera = input("Seleccione una carrera para el curso (ingrese el número): ")
        if seleccion_carrera.isnumeric():
            seleccion_carrera = int(seleccion_carrera)
            if 1 <= seleccion_carrera <= len(carreras):
                carrera_seleccionada = carreras[seleccion_carrera - 1]
                break
            elif seleccion_carrera == len(carreras) + 1:
                nueva_carrera_nombre = input("Ingrese el nombre de la nueva carrera: ")
                carrera_seleccionada = Carrera(nueva_carrera_nombre)
                carreras.append(carrera_seleccionada)
                print(f"Nueva carrera '{nueva_carrera_nombre}' creada.")
                break
            else:
                print("Selección inválida. Ingrese un número válido.")
        else:
            print("Selección inválida. Ingrese un número válido.")
    
    curso_nombre = input("Ingrese el nombre del curso que va a dictar: ").capitalize()
    cursos_de_la_carrera = carrera_seleccionada.get_cursos()
    for curso in cursos_de_la_carrera:
        if curso.nombre.lower() == curso_nombre.lower():
            print(f"El curso {curso_nombre} ya existe en la lista, por favor ingrese otro")
            return
    
    #Crear una instancia de Curso para generar la contraseña
    clave_matriculacion = Curso.generar_clave()  # Llama al método desde la clase Curso
    nuevo_curso = Curso(curso_nombre, clave_matriculacion)
    
    # Agregar el curso a la lista de cursos de la carrera
    carrera_seleccionada.agregar_curso(nuevo_curso)
    profesor.cursos.append(nuevo_curso)
    
    print(f"Curso ingresado con exito!, \nCurso: {curso_nombre}\nCarrera: {carrera_seleccionada.nombre}\nClave Matriculacion: {clave_matriculacion}\nCódigo del Curso: {nuevo_curso.codigo}")
    
    
def cursos_dictados(profesor_encontrado):
    if not profesor_encontrado.cursos:
        print("Aun no tienes registrado un curso para dictar.")
    else:
        print("Cursos inscriptos para dictar.")
        for i, curso in enumerate(profesor_encontrado.cursos, start=1):
            print(f"{i}.- {curso.nombre}")
            
        opcion = input("Seleccione el número del curso para ver más detalles: ")
        if opcion.isnumeric():
            indice_curso = int(opcion) - 1
            if 0 <= indice_curso < len(profesor_encontrado.cursos):
                curso_seleccionado = profesor_encontrado.cursos[indice_curso]
                cantidad_archivos = len(curso_seleccionado.archivos) if hasattr(curso_seleccionado, 'archivos') else 0
                print(f"{i}.- {curso.nombre} - Código: {curso.codigo} - Clave de Matriculación: {curso.clave} - Cantidad de Archivos: {cantidad_archivos}")
                #Agregar archivos
                respuesta = input("¿Desea agregar un archivo adjunto? (S/N): ").strip().lower()
                if respuesta == 's':
                    agregar_archivo_a_curso(curso_seleccionado)
            else:
                print("Opción no válida, por favor ingrese una opción que se encuentre en la lista.")
        else:
            print("Opción inválida, por favor ingrese una opción que sea numérica.")

def agregar_archivo_a_curso(curso):
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    formato_archivo = input("Ingrese el formato del archivo: ")
    formato_archivo_limpio = formato_archivo.replace(".", "")
    nuevo_archivo = Archivo(nombre_archivo, formato_archivo_limpio)
    curso.nuevo_archivo(nuevo_archivo)
    print("Archivo agregado con éxito.")

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
            ver_cursos(carreras, True)
        elif int(opcion) == 4:
            print("Saliendo del sistema..")
            break
        else:
            print("Ingrese una opción valida")
    else:
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para salir ")
    
print("Hasta luego!")
    