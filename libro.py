import cod_generator
# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}
libros = [libro1, libro2, libro3]
def nuevo_libro():
    cod = generar_codigo()
    cant_ej_ad = int(input("ingrese la cantidad de ejemplares disponibles: "))
    cant_ej_pr = int(input("ingrese la cantidad de ejemplares prestados: "))
    titulo = input("ingrese el titulo del libro: ")
    autor = input("ingrese el nombre del autor: ")
    libro = {'cod': cod, "cant_ej_ad": cant_ej_ad, "cant_ej_pr": cant_ej_pr, "titulo": titulo, "autor": autor}
    print(f"el codigo del libro {libro['titulo']} es {libro['cod']}")
    libros.append(libro)

def generar_codigo():
    #completar
    return cod_generator.generar()