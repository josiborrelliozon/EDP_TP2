import time
import random
import queue
from Apps import *

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

class ColaDeReproduccion: #Clase abstracta generadora de colas de reproduccion
    def __init__(self, capacidad_maxima=100):
        self.cola = queue.Queue(maxsize=capacidad_maxima) #Crea una cola con capacidad máxima de 100 canciones


class SpotifyApp(App):
    canciones_creadas = []  # Lista estática de canciones creadas

    def __init__(self, nombre, espacio):
        super().__init__(nombre, espacio)
        self.canciones_guardadas = []  # Lista de canciones guardadas por los usuarios
        self.playlists = []  # Lista de playlists
        self._pausado = False
        self._cancion_actual = None
        self.cola_reproduccion = ColaDeReproduccion() #Crea una instancia de Cola_De_Reproduccion

#Primero muestro los metodos de cola

    def agregar_a_cola_reproduccion(self, cancion):
        """
        Agrega una canción a la cola de reproducción si no está llena.

        Verifica si la cola de reproducción tiene espacio disponible y agrega la canción
        si la cola no está llena. Si la cola está llena, muestra un mensaje indicando
        que no se puede agregar más canciones.

        Parámetros:
        ----------
        cancion : Canción
            Objeto que representa la canción que se desea agregar a la cola de reproducción.
        """

        # Agrega una canción a la cola de reproducción si no está llena.
        if not self.cola_reproduccion.cola.full():
            self.cola_reproduccion.cola.put(cancion)
            print(f"Canción '{cancion.nombre}' agregada a la cola de reproducción.")
        else:
            print("La cola de reproducción está llena. No se puede agregar más canciones.")

    def reproducir_cola(self):
        """
        Reproduce todas las canciones de la cola de reproducción.

        Extrae y reproduce cada canción en la cola de reproducción, esperando la duración
        de cada una antes de pasar a la siguiente. Al finalizar, muestra un mensaje indicando
        que la cola de reproducción está vacía.

        Parámetros:
        ----------
        Ninguno
        """

        # Reproduce todas las canciones de la cola de reproducción.
        while not self.cola_reproduccion.cola.empty():
            cancion = self.cola_reproduccion.cola.get()
            if cancion:
                self.reproducir_cancion(cancion)  # Reproducir la canción
                time.sleep(cancion.duracion)  # Esperar durante la duración de la canción
        print("La cola de reproducción está vacía.")

    def ver_cola(self):
        """
        Muestra las canciones en la cola de reproducción.

        Verifica si la cola de reproducción está vacía y, si no lo está, muestra una lista
        numerada de las canciones en la cola. Si la cola está vacía, muestra un mensaje indicándolo.

        Parámetros:
        ----------
        Ninguno
        """

        # Muestra las canciones en la cola de reproducción.
        if not self.cola_reproduccion.cola.empty():
            print("Canciones en la cola de reproducción:")
            for idx, cancion in enumerate(list(self.cola_reproduccion.cola.queue), 1):
                print(f"{idx}. {cancion}")
        else:
            print("La cola de reproducción está vacía.")

#Acá muestro otros métodos con listas. Después se usan para la interfaz interactiva

    def agregar_cancion_guardada(self, cancion):
        """
        Agrega una canción a la lista de canciones guardadas si está en la lista de canciones creadas.

        Verifica si la canción existe en la lista de canciones creadas y si no está ya guardada.
        Si se cumple ambas condiciones, la canción se agrega a la lista de canciones guardadas.
        Si la canción ya está guardada o no está creada, se muestra un mensaje correspondiente.

        Parámetros:
        ----------
        cancion : Canción
            Objeto que representa la canción que se desea guardar.
        """

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
        """
        Elimina una canción de la lista de canciones guardadas.

        Verifica si la canción está en la lista de canciones guardadas y, si es así,
        la elimina. Si la canción no está en la lista, muestra un mensaje indicando que no se encuentra.

        Parámetros:
        ----------
        cancion : Canción
            Objeto que representa la canción que se desea eliminar de las canciones guardadas.
        """

        # Eliminar una canción de la lista de canciones guardadas
        if cancion in self.canciones_guardadas:
            self.canciones_guardadas.remove(cancion)
            print(f"Canción {cancion} eliminada de las canciones guardadas.")
        else:
            print(f"La canción {cancion} no está en la lista de canciones guardadas.")


    def crear_playlist(self, nombre_playlist):
        """
        Crea una nueva playlist y la agrega a la lista de playlists.

        Crea un objeto `Playlist` con el nombre proporcionado y lo agrega a la lista de playlists.
        Muestra un mensaje confirmando la creación de la playlist.

        Parámetros:
        ----------
        nombre_playlist : str
            Nombre de la nueva playlist a crear.
        """
        nueva_playlist = Playlist(nombre_playlist)
        self.playlists.append(nueva_playlist)
        print(f"Playlist '{nombre_playlist}' creada.")


    def eliminar_playlist(self, nombre_playlist):
        """
        Elimina una playlist de la lista de playlists.

        Busca una playlist con el nombre proporcionado (ignorando mayúsculas y minúsculas)
        y la elimina de la lista de playlists. Si no se encuentra la playlist, muestra un mensaje indicando que no fue encontrada.

        Parámetros:
        ----------
        nombre_playlist : str
            Nombre de la playlist que se desea eliminar.
        """

        # Eliminar una playlist de la lista de playlists
        for playlist in self.playlists:
            if playlist.nombre.lower() == nombre_playlist.lower():
                self.playlists.remove(playlist)
                print(f"Playlist '{nombre_playlist}' eliminada.")
                return
        print(f"No se encontró la playlist '{nombre_playlist}'.")


    def agregar_cancion_a_playlist(self, nombre_playlist, cancion):
        """
        Agrega una canción a una playlist existente.

        Verifica si la canción está en la lista de canciones creadas y si la playlist existe.
        Si ambos son ciertos, agrega la canción a la playlist. Si la canción ya está en la playlist
        o la playlist no se encuentra, muestra un mensaje correspondiente.

        Parámetros:
        ----------
        nombre_playlist : str
            Nombre de la playlist a la que se desea agregar la canción.
        cancion : Canción
            Objeto que representa la canción que se desea agregar a la playlist.
        """

        if cancion in SpotifyApp.canciones_creadas:  # Verificar si la canción está en la lista de canciones creadas
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
        """
        Elimina una canción de una playlist específica.

        Busca la playlist con el nombre proporcionado y, si la canción está en la playlist,
        la elimina. Si la canción no está en la playlist o la playlist no se encuentra,
        muestra un mensaje correspondiente.

        Parámetros:
        ----------
        nombre_playlist : str
            Nombre de la playlist de la que se desea eliminar la canción.
        cancion : Canción
            Objeto que representa la canción que se desea eliminar de la playlist.
        """

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
        """
        Muestra todas las playlists almacenadas.

        Verifica si hay playlists y, si existen, las muestra en una lista numerada.
        Si no hay playlists, muestra un mensaje indicando que no hay playlists disponibles.

        Parámetros:
        ----------
        Ninguno
        """

        if not self.playlists:
            print("No hay playlists.")
        else:
            print("Playlists:")
            for idx, playlist in enumerate(self.playlists, 1):
                print(f"{idx}. {playlist}")


    def ver_canciones_guardadas(self):
        """
        Muestra todas las canciones guardadas.

        Verifica si hay canciones guardadas y, si existen, las muestra en una lista numerada.
        Si no hay canciones guardadas, muestra un mensaje indicando que no hay canciones guardadas.

        Parámetros:
        ----------
        Ninguno
        """

        if not self.canciones_guardadas:
            print("No hay canciones guardadas.")
        else:
            print("Canciones Guardadas:")
            for idx, cancion in enumerate(self.canciones_guardadas, 1):
                print(f"{idx}. {cancion}")

    def ver_canciones_creadas(self):
        """
        Muestra todas las canciones creadas.

        Verifica si existen canciones creadas en `SpotifyApp.canciones_creadas` y, si es así,
        las muestra en una lista numerada. Si no hay canciones creadas, muestra un mensaje indicando que no hay canciones.

        Parámetros:
        ----------
        Ninguno
        """

        if not SpotifyApp.canciones_creadas:
            print("No hay canciones creadas.")
        else:
            print("Canciones Creadas:")
            for idx, cancion in enumerate(SpotifyApp.canciones_creadas, 1):
                print(f"{idx}. {cancion}")


    def ver_canciones_de_playlist(self, nombre_playlist):
        """
        Muestra las canciones de una playlist específica.

        Busca la playlist con el nombre proporcionado y, si existe, muestra las canciones que contiene.
        Si la playlist está vacía, muestra un mensaje indicando que no tiene canciones. Si no se encuentra la playlist, muestra un mensaje correspondiente.

        Parámetros:
        ----------
        nombre_playlist : str
            Nombre de la playlist de la cual se desea ver las canciones.
        """

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
        """
        Reproduce las canciones de una playlist.

        Busca la playlist con el nombre proporcionado y, si la playlist no está vacía,
        reproduce las canciones. Si el parámetro `aleatorio` es `True`, las canciones se reproducen
        en orden aleatorio. Si la playlist está vacía o no se encuentra, muestra un mensaje correspondiente.

        Parámetros:
        ----------
        nombre_playlist : str
            Nombre de la playlist que se desea reproducir.
        aleatorio : bool, opcional
            Si se establece como `True`, las canciones se reproducen en orden aleatorio (por defecto es `False`).
        """

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
        """
        Reproduce una canción de la lista de canciones guardadas.

        Busca la canción con el nombre proporcionado en la lista de canciones guardadas y, si la encuentra,
        la reproduce. Si no se encuentra la canción, muestra un mensaje correspondiente.

        Parámetros:
        ----------
        nombre_cancion : str
            Nombre de la canción que se desea reproducir.
        """

        # Reproducir una canción de las canciones guardadas
        for cancion in self.canciones_guardadas:
            if cancion.nombre.lower() == nombre_cancion.lower():
                self.reproducir_cancion(cancion)
                time.sleep(cancion.duracion)  # Simular la duración de la canción
                return
        print(f"No se encontró la canción '{nombre_cancion}' en las canciones guardadas.")


    def reproducir_cancion(self, cancion):
        """
        Reproduce una canción.

        Muestra un mensaje indicando que la canción proporcionada está siendo reproducida.

        Parámetros:
        ----------
        cancion : Canción
            Objeto que representa la canción que se desea reproducir.
        """

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




