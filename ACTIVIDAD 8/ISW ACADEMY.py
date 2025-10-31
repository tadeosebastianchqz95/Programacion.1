# ISW Academy
# Autor: Tadeo
# Descripción: Programa para administrar cursos, instructores y alumnos.

def mostrar_menu():
    print("\n=== ISW ACADEMY ===")
    print("1. Agregar curso")
    print("2. Eliminar curso")
    print("3. Modificar curso")
    print("4. Mostrar información de cursos")
    print("5. Mostrar cantidad de alumnos por curso")
    print("6. Cambiar instructor / aula / alumnos")
    print("7. Mostrar lista de alumnos de un curso")
    print("8. Salir")

def mostrar_cursos(cursos):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        for i, curso in enumerate(cursos):
            print(f"{i+1}. {curso['nombre']} (Aula: {curso['aula']}, Instructor: {curso['instructor']})")

def main():
    cursos = []

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            # Agregar curso
            nombre = input("Nombre del curso: ")
            aula = input("Aula: ")
            instructor = input("Instructor: ")
            alumnos = input("Lista de alumnos (separados por coma): ").split(",")
            alumnos = [a.strip() for a in alumnos]
            curso = {"nombre": nombre, "aula": aula, "instructor": instructor, "alumnos": alumnos}
            cursos.append(curso)
            print("✅ Curso agregado correctamente.")

        elif opcion == "2":
            # Eliminar curso
            mostrar_cursos(cursos)
            indice = int(input("Número del curso a eliminar: ")) - 1
            if 0 <= indice < len(cursos):
                cursos.pop(indice)
                print("✅ Curso eliminado.")
            else:
                print("⚠️ Opción no válida.")

        elif opcion == "3":
            # Modificar curso
            mostrar_cursos(cursos)
            indice = int(input("Número del curso a modificar: ")) - 1
            if 0 <= indice < len(cursos):
                curso = cursos[indice]
                curso["nombre"] = input(f"Nuevo nombre ({curso['nombre']}): ") or curso["nombre"]
                curso["aula"] = input(f"Nueva aula ({curso['aula']}): ") or curso["aula"]
                curso["instructor"] = input(f"Nuevo instructor ({curso['instructor']}): ") or curso["instructor"]
                print("✅ Curso modificado correctamente.")
            else:
                print("⚠️ Curso no encontrado.")

        elif opcion == "4":
            # Mostrar información de cursos
            mostrar_cursos(cursos)

        elif opcion == "5":
            # Mostrar cantidad de alumnos por curso
            for curso in cursos:
                print(f"{curso['nombre']}: {len(curso['alumnos'])} alumnos inscritos")

        elif opcion == "6":
            # Cambiar instructor, aula o alumnos
            mostrar_cursos(cursos)
            indice = int(input("Número del curso a editar: ")) - 1
            if 0 <= indice < len(cursos):
                curso = cursos[indice]
                print("\n1. Cambiar instructor")
                print("2. Cambiar aula")
                print("3. Agregar alumno")
                print("4. Dar de baja alumno")
                sub = input("Seleccione una opción: ")

                if sub == "1":
                    curso["instructor"] = input("Nuevo instructor: ")
                elif sub == "2":
                    curso["aula"] = input("Nueva aula: ")
                elif sub == "3":
                    alumno = input("Nombre del alumno a agregar: ")
                    curso["alumnos"].append(alumno)
                    print("✅ Alumno agregado.")
                elif sub == "4":
                    alumno = input("Nombre del alumno a eliminar: ")
                    if alumno in curso["alumnos"]:
                        curso["alumnos"].remove(alumno)
                        print("✅ Alumno eliminado.")
                    else:
                        print("⚠️ Alumno no encontrado.")
                else:
                    print("⚠️ Opción no válida.")
            else:
                print("⚠️ Curso no encontrado.")

        elif opcion == "7":
            # Mostrar lista de alumnos de un curso
            mostrar_cursos(cursos)
            indice = int(input("Número del curso: ")) - 1
            if 0 <= indice < len(cursos):
                print(f"Alumnos en {cursos[indice]['nombre']}:")
                for alumno in cursos[indice]['alumnos']:
                    print(f"- {alumno}")
            else:
                print("⚠️ Curso no encontrado.")

        elif opcion == "8":
            print("👋 Programa finalizado. ¡Gracias por usar ISW Academy!")
            break

        else:
            print("⚠️ Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()