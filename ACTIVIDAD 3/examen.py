# Quiz del examen de Programación I

preguntas = [
    {
        "pregunta": "1. ¿Qué estructura de control es más adecuada para iterar sobre una secuencia de elementos con un número de veces conocido de antemano?",
        "opciones": ["A) Bucle 'para'", "B) Sentencia condicional 'Si'", "C) Bucle 'repetir'", "D) Bucle 'mientras'"],
        "respuesta": "A"
    },
    {
        "pregunta": "2. ¿Qué es un algoritmo?",
        "opciones": ["A) Un conjunto de instrucciones escritas en código binario",
                     "B) Un lenguaje de programación específico",
                     "C) El código fuente de un programa de computadora",
                     "D) Una secuencia de pasos finitos y bien definidos para resolver un problema"],
        "respuesta": "D"
    },
    {
        "pregunta": "3. El lenguaje máquina está compuesto por:",
        "opciones": ["A) Símbolos lógicos y matemáticos",
                     "B) Pseudocódigo",
                     "C) Instrucciones en inglés abreviado",
                     "D) Código binario"],
        "respuesta": "D"
    },
    {
        "pregunta": "4. ¿Cuál de los siguientes componentes NO es parte fundamental de la arquitectura de Von Neumann?",
        "opciones": ["A) Sistema de entrada/salida", "B) CPU", "C) Tarjeta gráfica", "D) Memoria principal"],
        "respuesta": "C"
    },
    {
        "pregunta": "5. Un lenguaje de programación de alto nivel se caracteriza por:",
        "opciones": ["A) Ser más rápido en tiempo de ejecución",
                     "B) Tener un control directo y preciso sobre el hardware",
                     "C) Ser independiente de la arquitectura de la computadora",
                     "D) Ser más lento que el lenguaje máquina"],
        "respuesta": "C"
    },
    {
        "pregunta": "6. El lenguaje Java es considerado un lenguaje de nivel:",
        "opciones": ["A) Bajo", "B) Muy Alto", "C) Medio", "D) Alto"],
        "respuesta": "D"
    },
    {
        "pregunta": "7. Un programa de computadora es esencialmente:",
        "opciones": ["A) Una colección de algoritmos",
                     "B) El sistema operativo de una computadora",
                     "C) Un dispositivo de hardware",
                     "D) Una secuencia de instrucciones que la computadora ejecuta"],
        "respuesta": "D"
    },
    {
        "pregunta": "8. En pseudocódigo, ¿qué estructura de control se utiliza para ejecutar un bloque de código solo si se cumple una condición específica?",
        "opciones": ["A) Condicional o de selección",
                     "B) Repetitiva 'para'",
                     "C) Secuencial",
                     "D) Repetitiva 'mientras'"],
        "respuesta": "A"
    },
    {
        "pregunta": "9. El propósito principal del pseudocódigo es:",
        "opciones": ["A) Traducir automáticamente código de alto nivel a lenguaje máquina",
                     "B) Ejecutar programas de forma más eficiente que un lenguaje compilado",
                     "C) Planificar y describir la lógica de un algoritmo de forma legible para los humanos",
                     "D) Proporcionar un control directo sobre los registros del procesador"],
        "respuesta": "C"
    },
    {
        "pregunta": "10. ¿Cuál es la principal diferencia entre un bucle 'mientras' (while) y un bucle 'repetir' (do-while)?",
        "opciones": ["A) El bucle 'mientras' puede no ejecutarse, mientras que el 'repetir' se ejecuta al menos una vez",
                     "B) No hay ninguna diferencia, son intercambiables",
                     "C) El bucle 'mientras' es más rápido que el 'repetir'",
                     "D) El bucle 'repetir' solo usa números, mientras que el 'mientras' usa cualquier condición"],
        "respuesta": "A"
    }
]

puntaje = 0

print("=== Examen de Programación I ===\n")

for i, p in enumerate(preguntas, start=1):
    print(p["pregunta"])
    for opcion in p["opciones"]:
        print(opcion)
    respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
    if respuesta == p["respuesta"]:
        print("✅ Correcto!\n")
        puntaje += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {p['respuesta']}\n")

print(f"Tu puntaje final es: {puntaje} de {len(preguntas)}")