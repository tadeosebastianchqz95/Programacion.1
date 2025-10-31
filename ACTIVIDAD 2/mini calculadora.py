# Mini Calculadora Interactiva
# Autor: Tadeo
# Descripción: Calculadora sencilla con operaciones básicas

def mini_calculadora():
    print("🧮 Mini Calculadora Interactiva")
    print("------------------------------")

    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    try:
        opcion = int(input("Elige una opción (1-4): "))
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == 1:
            resultado = num1 + num2
            operacion = "+"
        elif opcion == 2:
            resultado = num1 - num2
            operacion = "-"
        elif opcion == 3:
            resultado = num1 * num2
            operacion = "×"
        elif opcion == 4:
            if num2 != 0:
                resultado = num1 / num2
                operacion = "÷"
            else:
                print("❌ Error: No se puede dividir entre cero.")
                return
        else:
            print("⚠️ Opción no válida.")
            return

        print(f"\nResultado: {num1} {operacion} {num2} = {resultado}")

    except ValueError:
        print("⚠️ Entrada no válida. Asegúrate de escribir números correctamente.")

    print("\n✅ Gracias por usar la Mini Calculadora Interactiva.")

# Ejecutar la calculadora
if __name__ == "__main__":
    mini_calculadora()