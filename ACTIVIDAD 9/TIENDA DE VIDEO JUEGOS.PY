#TIENDA DE VIDEO JUEGOS
info_tienda = ("¡Game On!", 2010)

inventario = {
    "The Legend of Zelda": {"precio": 1200, "stock": 5},
    "Super Mario Odyssey": {"precio": 1000, "stock": 3},
    "Minecraft": {"precio": 800, "stock": 10}
}

segundo_juego = list(inventario.keys())[1]  # obtiene la segunda clave del diccionario
print(f"El precio de '{segundo_juego}' es: ${inventario[segundo_juego]['precio']}")

primer_juego = list(inventario.keys())[0]
inventario[primer_juego]["stock"] -= 1
print(f"Vendiste una copia de '{primer_juego}'. Stock restante: {inventario[primer_juego]['stock']}")

print("\nInventario actualizado:")
for juego, datos in inventario.items():
    print(f"{juego} - Precio: ${datos['precio']} | Stock: {datos['stock']}")