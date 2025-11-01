from modelos.alumnos import agregar_alumno, eliminar_alumno, mostrar_alumnos


def crear_curso(nombre, instructor, aula):
    """Crea un curso nuevo."""
    return {"nombre": nombre, "instructor": instructor, "aula": aula, "alumnos": []}


def mostrar_cursos(cursos):
    """Muestra todos los cursos registrados."""
    print("\n Cursos registrados:")
    if not cursos:
        print("   No hay cursos disponibles.")
    else:
        for i, c in enumerate(cursos, 1):
            print(f" {i}. {c['nombre']} - Instructor: {c['instructor']} (Aula {c['aula']})")


def buscar_curso(cursos, nombre):
    """Busca un curso por nombre."""
    for curso in cursos:
        if curso["nombre"].lower() == nombre.lower():
            return curso
    return None


def agregar_alumno_a_curso(cursos, nombre_curso, alumno):
    """Agrega un alumno a un curso específico."""
    curso = buscar_curso(cursos, nombre_curso)
    if curso:
        agregar_alumno(curso["alumnos"], alumno)
    else:
        print(" Curso no encontrado.")


def eliminar_alumno_de_curso(cursos, nombre_curso, alumno):
    """Elimina un alumno de un curso."""
    curso = buscar_curso(cursos, nombre_curso)
    if curso:
        eliminar_alumno(curso["alumnos"], alumno)
    else:
        print(" Curso no encontrado.")


def mostrar_detalle_curso(cursos, nombre_curso):
    """Muestra los detalles y alumnos de un curso."""
    curso = buscar_curso(cursos, nombre_curso)
    if curso:
        print(f"\n Curso: {curso['nombre']}")
        print(f" Instructor: {curso['instructor']}")
        print(f" Aula: {curso['aula']}")
        mostrar_alumnos(curso["alumnos"])
    else:
        print(" Curso no encontrado.")
 