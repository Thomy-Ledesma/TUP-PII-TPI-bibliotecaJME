def ver_cursos(carreras):
    i = 1
    if not carreras:
        print("No hay cursos disponibles. Espere que el profesor lo de alta.")
    else:
        for carrera in carreras:
            print(f"{i} - {carrera.nombre}")
            i += 1
        carrera_seleccionada = int(input("Seleccione la carrera: ")) - 1
        i = 1
        for curso in carreras[carrera_seleccionada].cursos:
            print(f"{i} - {curso.nombre}")
            i += 1