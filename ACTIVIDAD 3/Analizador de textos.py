#Analizador De texto 

texto = input("Escribe un texto: ")
if "python" in texto.lower():
    print(" La palabra 'Python' fue encontrada en el texto.")
else:
    print(" La palabra 'Python' no se encontró en el texto.")

texto_minus = texto.lower()



contador = texto_minus.split().count("python")


palabras = texto.split()
invertido = " ".join(palabras[::-1])

print(f"\nLa palabra 'python' aparece {contador} veces.")
print("Texto invertido:")
print(invertido)



