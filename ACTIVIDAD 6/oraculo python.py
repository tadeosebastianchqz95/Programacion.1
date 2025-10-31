# Oráculo de Python
# Autor: Tadeo
# Descripción: Un oráculo digital que responde a tus preguntas con sabiduría y humor.

import random
import time

def oraculo_de_python():
    print("🐍🔮 Bienvenido al Oráculo de Python 🔮🐍")
    print("----------------------------------------")
    print("Haz una pregunta y recibirás la respuesta del gran Oráculo...\n")

    respuestas = [
        "La respuesta está en el código.",
        "Depura tus dudas, y hallarás la verdad.",
        "Eso... depende del contexto.",
        "Ni los dioses del stack overflow lo saben.",
        "Sí, pero revisa los paréntesis.",
        "No, porque hay un error de sintaxis.",
        "El bug está en tu corazón, no en el programa.",
        "Tal vez, si importas la librería correcta.",
        "Por supuesto, después de un 'try' y un 'except'.",
        "Esa variable aún no está definida.",
        "Sí... aunque probablemente te dé un warning.",
        "No mientras siga ese bucle infinito.",
        "Parece True, pero es un False disfrazado.",
        "Confía en Python... y en ti."
    ]

    while True:
        pregunta = input("🤔 Escribe tu pregunta (o 'salir' para terminar): ").strip().lower()

        if pregunta == "salir":
            print("\n🐍 El Oráculo se desconecta... hasta la próxima invocación 💤")
            break
        elif pregunta == "":
            print("⚠️ Debes formular una pregunta para recibir sabiduría.")
        else:
            print("\nConsultando a los dioses de Python", end="")
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.7)
            print("\n")
            print("💡 El Oráculo dice:", random.choice(respuestas))
            print("\n----------------------------------------")

# Ejecutar el programa
if __name__ == "__main__":
    oraculo_de_python()