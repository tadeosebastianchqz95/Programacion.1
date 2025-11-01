from modelos.cursos import (
    crear_curso,
    mostrar_cursos,
    agregar_alumno_a_curso,
    eliminar_alumno_de_curso,
    mostrar_detalle_curso,
)

def mostrar_menu():
    print("\n--**academia isw plus ultra**--")
    print("1. Crear curso")
    print("2. Mostrar cursos")
    print("3. Agregar alumno a curso")
    print("4. Eliminar alumno de curso")
    print("5. Ver detalle de curso")
    print("6. Salir")


def main():
    cursos = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del curso: ")
            instructor = input("Instructor: ")
            aula = input("Aula: ")
            cursos.append(crear_curso(nombre, instructor, aula))
            print(f" Curso '{nombre}' creado con éxito.")

        elif opcion == "2":
            mostrar_cursos(cursos)

        elif opcion == "3":
            nombre_curso = input("Nombre del curso: ")
            alumno = input("Nombre del alumno: ")
            agregar_alumno_a_curso(cursos, nombre_curso, alumno)

        elif opcion == "4":
            nombre_curso = input("Nombre del curso: ")
            alumno = input("Nombre del alumno a eliminar: ")
            eliminar_alumno_de_curso(cursos, nombre_curso, alumno)

        elif opcion == "5":
            nombre_curso = input("Nombre del curso: ")
            mostrar_detalle_curso(cursos, nombre_curso)

        elif opcion == "6":
            print(" Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("  Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
