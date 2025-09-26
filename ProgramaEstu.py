
afirmacion = True
Bienvenida = "Registra tus estudiantes"
estudiantes = []

Menu = """
-------------------------------------------------
|                                               |
           Gestor de estudiantes                |
|-----------------------------------------------|
|                                               |
|           1. Registra estudiante              |
|           2. Lista de estudiantes             |
|           3. Buscar Estudiante                |
|           4. Promedio de calificaciones       |
|           5. Salir                            |
|-----------------------------------------------|
"""

print(Bienvenida)

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    asignatura = input("Ingrese la asignatura: ")
    calificacion = float(input("Ingrese la nota: "))
    estudiante = (nombre, asignatura, calificacion)
    estudiantes.append(estudiante)
    print(f" Estudiante '{nombre}' registrado correctamente.")


def listar_estudiantes():
    for estudiante in estudiantes:
        nombre, asignatura, calificacion = estudiante
        print(f"Nombre: {nombre} | Asignatura: {asignatura} | Calificación: {calificacion}")


def buscar_estudiante():
    nombre_buscado = input("Ingrese el nombre del estudiante a buscar: ")
    for nombre, asignatura, calificacion in estudiantes:
        if nombre == nombre_buscado:
            print(f"Nombre: {nombre} | Asignatura: {asignatura} | Calificación: {calificacion}")


def calcular_promedio():
    total = sum(e[2] for e in estudiantes)
    promedio = total / len(estudiantes)
    print(promedio)



while afirmacion:
    print(Menu)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        listar_estudiantes()
    elif opcion == "3":
        buscar_estudiante()
    elif opcion == "4":
        calcular_promedio()
    elif opcion == "5":
        print("Gracias por registrar y gestionar sus estudiantes. ¡Hasta pronto!")
        afirmacion = False  
    else:
        print("Opción inválida. Intente nuevamente.")