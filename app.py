# Trabajo Práctico I - Programación II


import os, libro

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            codigo = input("ingrese el codigo del libro: ")
            for ejemplar in libro.libros:
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
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            #completar
            libro.nuevo_libro()
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")