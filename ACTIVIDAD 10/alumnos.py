def agregar_alumno(lista_alumnos, nombre):
    """Agrega un alumno a la lista."""
    if nombre not in lista_alumnos:
        lista_alumnos.append(nombre)
        print(f" Alumno '{nombre}' agregado correctamente.")
    else:
        print(f" El alumno '{nombre}' ya está registrado.")


def eliminar_alumno(lista_alumnos, nombre):
    """Elimina un alumno si existe."""
    if nombre in lista_alumnos:
        lista_alumnos.remove(nombre)
        print(f" Alumno '{nombre}' eliminado correctamente.")
    else:
        print(f" El alumno '{nombre}' no existe en la lista.")


def mostrar_alumnos(lista_alumnos):
    """Muestra todos los alumnos registrados."""
    print("\n Lista de alumnos:")
    if not lista_alumnos:
        print("   No hay alumnos registrados.")
    else:
        for alumno in lista_alumnos:
            print(f"   - {alumno}")
