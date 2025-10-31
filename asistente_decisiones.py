# Asistente de decisiones del día
# Autor: Tadeo
# Descripción: Ayuda al usuario a tomar pequeñas decisiones diarias

def asistente_decisiones():
    print("🧠 Asistente de Decisiones del Día 🕒")
    print("----------------------------------")

    estado_animo = input("¿Cómo te sientes hoy? (feliz, cansado, estresado, triste): ").lower()
    clima = input("¿Cómo está el clima? (soleado, nublado, lluvioso, frío): ").lower()
    tarea = input("¿Tienes muchas tareas o trabajo hoy? (sí/no): ").lower()

    print("\nAnalizando tus respuestas...\n")

    # Recomendaciones basadas en el estado de ánimo
    if estado_animo == "feliz":
        print("✨ ¡Genial! Aprovecha tu energía para hacer algo productivo o divertido.")
    elif estado_animo == "cansado":
        print("😴 Descansa un poco, toma una siesta corta o escucha música relajante.")
    elif estado_animo == "estresado":
        print("🧘 Haz una pausa, respira profundo o sal a caminar unos minutos.")
    elif estado_animo == "triste":
        print("💛 Habla con alguien de confianza o haz algo que te haga sonreír.")
    else:
        print("🙂 Mantén una actitud positiva sin importar cómo te sientas.")

    # Recomendaciones según el clima
    if clima == "soleado":
        print("☀️ Día perfecto para salir a caminar o hacer ejercicio al aire libre.")
    elif clima == "nublado":
        print("🌤 Día tranquilo, ideal para leer o ver una película.")
    elif clima == "lluvioso":
        print("🌧 Quédate en casa con una bebida caliente y algo acogedor.")
    elif clima == "frío":
        print("🧣 Abrígate bien y disfruta de algo calentito.")
    else:
        print("🌈 Cada clima tiene su encanto, aprovéchalo.")

    # Decisión final según carga de trabajo
    if tarea == "sí":
        print("📋 Organiza tus tareas por prioridad y no olvides darte descansos.")
    else:
        print("🎉 Aprovecha tu tiempo libre para relajarte o hacer algo nuevo.")

    print("\n✅ Recomendación final: Mantén una actitud positiva y cuida de ti mismo 💪")

# Ejecutar el asistente
asistente_decisiones()