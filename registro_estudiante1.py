def mostrar_menu():
    print("\n--- SISTEMA DE REGISTRO ESTUDIANTIL ---")
    print("1. Registrar un estudiante.")
    print("2. Mostrar todos los estudiantes registrados.")
    print("3. Consultar el promedio de un estudiante.")
    print("4. Mostrar estadísticas generales del grupo.")
    print("5. Salir del programa.")
    print("6. Eliminar un estudiante (Extra).")

def calcular_promedio(notas):
    promedio = sum(notas) / 3
    return promedio

def registrar_estudiante(estudiantes):
    print("\n--- Registrar Estudiante ---")
    while True:
        id_alumno = input("ID del alumno: ").strip()
        if id_alumno == "":
            print("Error: El ID no puede quedar vacío.")
            continue
        
        repetido = False
        for est in estudiantes:
            if est["id"] == id_alumno:
                repetido = True
                break
        
        if repetido:
            print("Error: Ya existe un estudiante registrado con ese ID.")
        else:
            break

    while True:
        nombre_alumno = input("Nombre del alumno: ").strip()
        if nombre_alumno == "":
            print("Error: El nombre no puede quedar vacío.")
        else:
            break

    while True:
        cal1 = float(input("Ingrese la primera calificación (0-100): "))
        if cal1 >= 0 and cal1 <= 100:
            break
        else:
            print("Error: La calificación debe estar entre 0 y 100.")

    while True:
        cal2 = float(input("Ingrese la segunda calificación (0-100): "))
        if cal2 >= 0 and cal2 <= 100:
            break
        else:
            print("Error: La calificación debe estar entre 0 y 100.")

    while True:
        cal3 = float(input("Ingrese la tercera calificación (0-100): "))
        if cal3 >= 0 and cal3 <= 100:
            break
        else:
            print("Error: La calificación debe estar entre 0 y 100.")

    calificaciones = (cal1, cal2, cal3)
    
    promedio = calcular_promedio(calificaciones)

    if promedio >= 70:
        situacion = "Aprobado"
    else:
        situacion = "Reprobado"

    nuevo_estudiante = {
        "id": id_alumno,
        "nombre": nombre_alumno,
        "calificaciones": calificaciones,
        "promedio": promedio,
        "situacion": situacion
    }
    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante {nombre_alumno} registrado con éxito. Promedio: {promedio:.2f} ({situacion})")

def mostrar_estudiantes(estudiantes):
    print("\n--- Estudiantes Registrados ---")
    if len(estudiantes) == 0:
        print("Aún no hay estudiantes registrados.")
    else:
        for est in estudiantes:
            print(f"ID: {est['id']} | Nombre: {est['nombre']} | Calificaciones: {est['calificaciones']} | Promedio: {est['promedio']:.2f} | Situación: {est['situacion']}")

def consultar_estudiante(estudiantes):
    print("\n--- Consultar Promedio de Estudiante ---")
    if len(estudiantes) == 0:
        print("Aún no hay estudiantes registrados.")
        return

    id_buscar = input("Ingrese el ID del estudiante a buscar: ").strip()
    encontrado = False

    for est in estudiantes:
        if est["id"] == id_buscar:
            print(f"Estudiante: {est['nombre']}")
            print(f"Promedio: {est['promedio']:.2f}")
            print(f"Situación académica: {est['situacion']}")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún estudiante con ese ID.")

def mostrar_estadisticas(estudiantes):
    print("\n--- Estadísticas Generales del Grupo ---")
    if len(estudiantes) == 0:
        print("Aún no hay estudiantes registrados para calcular estadísticas.")
        return

    total_estudiantes = len(estudiantes)
    suma_promedios = 0
    aprobados = 0
    reprobados = 0
    promedio_mas_alto = 0

    for est in estudiantes:
        suma_promedios += est["promedio"]
        
        if est["situacion"] == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1

        if est["promedio"] > promedio_mas_alto:
            promedio_mas_alto = est["promedio"]

    promedio_general = suma_promedios / total_estudiantes

    print(f"Estudiantes registrados: {total_estudiantes}")
    print(f"Promedio general del grupo: {promedio_general:.2f}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Promedio más alto: {promedio_mas_alto:.2f}")

def eliminar_estudiante(estudiantes):
    print("\n--- Eliminar Estudiante ---")
    if len(estudiantes) == 0:
        print("Aún no hay estudiantes registrados.")
        return

    id_eliminar = input("Ingrese el ID del estudiante a eliminar: ").strip()
    encontrado = False

    for est in estudiantes:
        if est["id"] == id_eliminar:
            estudiantes.remove(est)
            print(f"El estudiante {est['nombre']} (ID: {id_eliminar}) fue eliminado.")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún estudiante con ese ID.")

estudiantes = []

while True:
    mostrar_menu()
    pregunta = input("Elija una opción (1-6): ").strip()

    if pregunta == "1":
        registrar_estudiante(estudiantes)
    elif pregunta == "2":
        mostrar_estudiantes(estudiantes)
    elif pregunta == "3":
        consultar_estudiante(estudiantes)
    elif pregunta == "4":
        mostrar_estadisticas(estudiantes)
    elif pregunta == "5":
        print("Saliendo del programa... ¡Hasta luego!")
        break
    elif pregunta == "6":
        eliminar_estudiante(estudiantes)
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 6.")