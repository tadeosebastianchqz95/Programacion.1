# Playlist de Música Mejorada 🎵
# Autor: Tadeo
# Descripción: Maneja una playlist con operaciones de lista, de forma diferente al ejemplo original.

def playlist_mejorada():
    # Lista inicial
    playlist_musica = ["Blinding Lights", "Bohemian Rhapsody", "Smells Like Teen Spirit"]
    print("🎶 Playlist inicial:", playlist_musica)

    # Función para agregar canción al final
    def agregar_cancion(cancion):
        playlist_musica.append(cancion)
        print(f"✅ '{cancion}' agregada al final de la playlist.")

    # Función para reemplazar una canción por otra
    def reemplazar_cancion(vieja, nueva):
        if vieja in playlist_musica:
            playlist_musica[playlist_musica.index(vieja)] = nueva
            print(f"🔄 '{vieja}' reemplazada por '{nueva}'.")
        else:
            print(f"⚠️ '{vieja}' no se encontró en la playlist.")

    # Función para insertar canción en posición específica
    def insertar_cancion(pos, cancion):
        if pos < 0 or pos > len(playlist_musica):
            print("⚠️ Posición inválida. Se agregará al final.")
            playlist_musica.append(cancion)
        else:
            playlist_musica.insert(pos, cancion)
        print(f"➕ '{cancion}' insertada en la posición {pos}.")

    # Manipulaciones diferentes al ejemplo original
    agregar_cancion("Levitating")
    reemplazar_cancion("Bohemian Rhapsody", "Shape of You")
    insertar_cancion(1, "Watermelon Sugar")
    eliminada = playlist_musica.pop(2)
    print(f"❌ Se eliminó la canción en la posición 2: '{eliminada}'")

    # Mostrar playlist final y número de canciones
    print("\n🎵 Playlist final:", playlist_musica)
    print("🎶 Número total de canciones:", len(playlist_musica))

# Ejecutar la función
if __name__ == "__main__":
    playlist_mejorada()