from libro import *

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(libro1)
libros.append(libro2)
libros.append(libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = crear_libro()
    libros.append(nuevo_libro)

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    codigo = input("ingrese el codigo del libro: ")
    for ejemplar in libros:
        if(codigo == ejemplar['cod']):    
            print(f"libro: {ejemplar['titulo']}")
            print(f"autor: {ejemplar['autor']}")
            print(f"ejemplares disponibles: {ejemplar['cant_ej_ad']}\n")
            if(ejemplar["cant_ej_ad"] > 0):
                ejemplar["cant_ej_ad"] -= 1
                ejemplar["cant_ej_pr"] += 1
                print("prestamo realizado con exito")
            else:
                print("no hay ejemplares disponibles")
            break

def devolver_ejemplar_libro():
    codigo = input("ingrese el codigo del libro: ")
    for ejemplar in libros:
        if(codigo == ejemplar['cod']):    
            print(f"libro: {ejemplar['titulo']}")
            print(f"autor: {ejemplar['autor']}")
            print(f"ejemplares disponibles: {ejemplar['cant_ej_ad']}\n")
            if(ejemplar["cant_ej_pr"] > 0):
                ejemplar["cant_ej_pr"] -= 1
                ejemplar["cant_ej_ad"] += 1
                print("devolución realizada con exito")
            else:
                print("no hay ejemplares a devolver")
            break

def crear_libro():
    cod = generar_codigo()
    cant_ej_ad = int(input("ingrese la cantidad de ejemplares disponibles: "))
    cant_ej_pr = int(input("ingrese la cantidad de ejemplares prestados: "))
    titulo = input("ingrese el titulo del libro: ")
    autor = input("ingrese el nombre del autor: ")
    print(f"el codigo del libro {titulo} es {cod}")
    return {'cod': cod, "cant_ej_ad": cant_ej_ad, "cant_ej_pr": cant_ej_pr, "titulo": titulo, "autor": autor}

