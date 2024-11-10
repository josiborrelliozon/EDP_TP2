import time
import random


class App:
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio

    def __str__(self):
        return f'{self.nombre}, espacio = {self.espacio} Gb'


class Cancion:
    def __init__(self, nombre, artista, duracion, genero):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion  # Duración en segundos
        self.genero = genero

        # Agregar la canción automáticamente a la lista de canciones creadas en SpotifyApp
        SpotifyApp.canciones_creadas.append(self)

    def __str__(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{self.nombre} de {self.artista} ({minutos} min {segundos} seg) - Género: {self.genero}"


class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []  # Lista de canciones en la playlist

    def __str__(self):
        if not self.canciones:
            return f"Playlist {self.nombre} está vacía."

        # Calcular la duración total de la playlist directamente aquí
        total_duracion = sum(cancion.duracion for cancion in self.canciones)
        minutos = total_duracion // 60
        segundos = total_duracion % 60
        duracion_str = f"Duración estimada: {minutos} min {segundos} seg"

        canciones_str = "\n".join([f"{idx + 1}. {cancion}" for idx, cancion in enumerate(self.canciones)])
        return f"Playlist: {self.nombre}\n{canciones_str}\n{duracion_str}"


class SpotifyApp(App):
    canciones_creadas = []  # Lista estática de canciones creadas

    def __init__(self, nombre, espacio):
        super().__init__(nombre, espacio)
        self.canciones_guardadas = []  # Lista de canciones guardadas por los usuarios
        self.playlists = []  # Lista de playlists
        self._pausado = False
        self._cancion_actual = None

    def agregar_cancion_guardada(self, cancion):
        # Verificar si la canción está en la lista de canciones creadas
        if cancion in SpotifyApp.canciones_creadas:
            if cancion not in self.canciones_guardadas:
                self.canciones_guardadas.append(cancion)
                print(f"Canción {cancion} guardada.")
            else:
                print(f"La canción {cancion} ya está guardada.")
        else:
            print(f"La canción {cancion} no está creada. No se puede guardar.")

    def eliminar_cancion_guardada(self, cancion):
        # Eliminar una canción de la lista de canciones guardadas
        if cancion in self.canciones_guardadas:
            self.canciones_guardadas.remove(cancion)
            print(f"Canción {cancion} eliminada de las canciones guardadas.")
        else:
            print(f"La canción {cancion} no está en la lista de canciones guardadas.")

    def crear_playlist(self, nombre_playlist):
        nueva_playlist = Playlist(nombre_playlist)
        self.playlists.append(nueva_playlist)
        print(f"Playlist '{nombre_playlist}' creada.")

    def eliminar_playlist(self, nombre_playlist):
        # Eliminar una playlist de la lista de playlists
        for playlist in self.playlists:
            if playlist.nombre.lower() == nombre_playlist.lower():
                self.playlists.remove(playlist)
                print(f"Playlist '{nombre_playlist}' eliminada.")
                return
        print(f"No se encontró la playlist '{nombre_playlist}'.")

    def agregar_cancion_a_playlist(self, nombre_playlist, cancion):

        if cancion in SpotifyApp.canciones_creadas: # Verificar si la canción está en la lista de canciones creadas
            for playlist in self.playlists:
                if playlist.nombre.lower() == nombre_playlist.lower():
                    if cancion not in playlist.canciones:
                        playlist.canciones.append(cancion)
                        print(f"Canción {cancion} agregada a la playlist '{nombre_playlist}'.")
                    else:
                        print(f"La canción {cancion} ya está en la playlist '{nombre_playlist}'.")
                    return
            print(f"No se encontró la playlist '{nombre_playlist}'.")
        else:
            print(f"La canción {cancion} no está creada. No se puede agregar a la playlist.")

    def eliminar_cancion_de_playlist(self, nombre_playlist, cancion):
        # Eliminar una canción de una playlist específica
        for playlist in self.playlists:
            if playlist.nombre.lower() == nombre_playlist.lower():
                if cancion in playlist.canciones:
                    playlist.canciones.remove(cancion)
                    print(f"Canción {cancion} eliminada de la playlist '{nombre_playlist}'.")
                else:
                    print(f"La canción {cancion} no está en la playlist '{nombre_playlist}'.")
                return
        print(f"No se encontró la playlist '{nombre_playlist}'.")

    def ver_playlists(self):
        if not self.playlists:
            print("No hay playlists.")
        else:
            print("Playlists:")
            for idx, playlist in enumerate(self.playlists, 1):
                print(f"{idx}. {playlist}")

    def ver_canciones_guardadas(self):
        if not self.canciones_guardadas:
            print("No hay canciones guardadas.")
        else:
            print("Canciones Guardadas:")
            for idx, cancion in enumerate(self.canciones_guardadas, 1):
                print(f"{idx}. {cancion}")

    def ver_canciones_creadas(self):
        if not SpotifyApp.canciones_creadas:
            print("No hay canciones creadas.")
        else:
            print("Canciones Creadas:")
            for idx, cancion in enumerate(SpotifyApp.canciones_creadas, 1):
                print(f"{idx}. {cancion}")

    def ver_canciones_de_playlist(self, nombre_playlist):
        for playlist in self.playlists:
            if playlist.nombre.lower() == nombre_playlist.lower():
                if not playlist.canciones:
                    print(f"La playlist '{nombre_playlist}' está vacía.")
                else:
                    print(f"Las canciones de la playlist '{nombre_playlist}' son:")
                    for idx, cancion in enumerate(playlist.canciones, 1):
                        print(f"{idx}. {cancion}")
                return
        print(f"No se encontró la playlist '{nombre_playlist}'.")

    def reproducir_playlist(self, nombre_playlist, aleatorio=False):
        for playlist in self.playlists:
            if playlist.nombre.lower() == nombre_playlist.lower():
                if not playlist.canciones:
                    print(f"La playlist '{nombre_playlist}' está vacía.")
                else:
                    print(f"Reproduciendo la playlist '{nombre_playlist}'...")
                    canciones_a_reproducir = playlist.canciones[:]
                    if aleatorio:
                        random.shuffle(canciones_a_reproducir)

                    # Reproducir las canciones con time.sleep para simular la duración
                    for cancion in canciones_a_reproducir:
                        self.reproducir_cancion(cancion)
                        time.sleep(cancion.duracion)
                return
        print(f"No se encontró la playlist '{nombre_playlist}'.")

    def reproducir_cancion_guardada(self, nombre_cancion):
        # Reproducir una canción de las canciones guardadas
        for cancion in self.canciones_guardadas:
            if cancion.nombre.lower() == nombre_cancion.lower():
                self.reproducir_cancion(cancion)
                time.sleep(cancion.duracion)  # Simular la duración de la canción
                return
        print(f"No se encontró la canción '{nombre_cancion}' en las canciones guardadas.")

    def reproducir_cancion(self, cancion):
        print(f"Reproduciendo: {cancion}")


def menu():
    print("\nBienvenido a SpotifyApp Interactivo")
    print("1. Crear Playlist")
    print("2. Ver Playlists")
    print("3. Agregar Canción a Playlist")
    print("4. Eliminar Playlist")
    print("5. Ver Canciones Guardadas")
    print("6. Ver Canciones Creadas")
    print("7. Reproducir Playlist")
    print("8. Reproducir Canción Guardada")
    print("9. Salir")


def interfaz():
    app = SpotifyApp("Spotify", 100)  # Crear una instancia de SpotifyApp
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_playlist = input("Ingrese el nombre de la playlist: ")
            app.crear_playlist(nombre_playlist)
        elif opcion == "2":
            app.ver_playlists()
        elif opcion == "3":
            nombre_playlist = input("Ingrese el nombre de la playlist: ")
            app.ver_canciones_creadas()
            try:
                idx_cancion = int(input("Seleccione el número de la canción para agregar: ")) - 1
                cancion = SpotifyApp.canciones_creadas[idx_cancion]
                app.agregar_cancion_a_playlist(nombre_playlist, cancion)
            except (ValueError, IndexError):
                print("Selección inválida.")
        elif opcion == "4":
            nombre_playlist = input("Ingrese el nombre de la playlist a eliminar: ")
            app.eliminar_playlist(nombre_playlist)
        elif opcion == "5":
            app.ver_canciones_guardadas()
        elif opcion == "6":
            app.ver_canciones_creadas()
        elif opcion == "7":
            nombre_playlist = input("Ingrese el nombre de la playlist para reproducir: ")
            aleatorio = input("¿Reproducir aleatoriamente? (s/n): ").lower() == "s"
            app.reproducir_playlist(nombre_playlist, aleatorio)
        elif opcion == "8":
            nombre_cancion = input("Ingrese el nombre de la canción guardada para reproducir: ")
            app.reproducir_cancion_guardada(nombre_cancion)
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")



if __name__ == "__main__":
    # Crear la aplicación Spotify
    app = SpotifyApp("Spotify", 10)  # 10 Gb de espacio

    # Crear algunas canciones
    cancion1 = Cancion("Shape of You", "Ed Sheeran", 240, "Pop")
    cancion2 = Cancion("Blinding Lights", "The Weeknd", 200, "Pop")
    cancion3 = Cancion("Stay", "The Kid LAROI, Justin Bieber", 150, "Pop")

    # Crear una playlist
    app.crear_playlist("Mi Playlist Favorita")

    # Agregar canciones a la playlist
    app.agregar_cancion_a_playlist("Mi Playlist Favorita", cancion1)
    app.agregar_cancion_a_playlist("Mi Playlist Favorita", cancion2)
    app.agregar_cancion_a_playlist("Mi Playlist Favorita", cancion3)

    # Ver las playlists y canciones creadas
    app.ver_playlists()
    app.ver_canciones_creadas()

    # Reproducir la playlist (sin aleatorio)
    app.reproducir_playlist("Mi Playlist Favorita")

    # Reproducir una canción guardada
    app.agregar_cancion_guardada(cancion1)
    app.reproducir_cancion_guardada("Shape of You")

    # Reproducir la playlist con aleatorio
    app.reproducir_playlist("Mi Playlist Favorita", aleatorio=True)

    interfaz()




