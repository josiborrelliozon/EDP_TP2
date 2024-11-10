import time

class Cancion:
    def __init__(self, nombre, artista, duracion, genero):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion  # Duración en segundos
        self.genero = genero

    def __str__(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{self.nombre} de {self.artista} ({minutos} min {segundos} seg) - Género: {self.genero}"

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []  # Lista de canciones en la playlist

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def mostrar_playlist(self):
        if not self.canciones:
            print(f"Playlist {self.nombre} está vacía.")
        else:
            print(f"Playlist: {self.nombre}")
            for idx, cancion in enumerate(self.canciones, 1):
                print(f"{idx}. {cancion}")

    def reproducir(self):
        if not self.canciones:
            print(f"La playlist {self.nombre} está vacía.")
        else:
            print(f"Reproduciendo la playlist {self.nombre}...")
            for cancion in self.canciones:
                print(f"Reproduciendo: {cancion}")
                # Esperamos según la duración de la canción (en segundos)
                time.sleep(cancion.duracion)

    def reproducir_cancion(self, nombre_cancion):
        # Busca la canción por nombre en la playlist
        for cancion in self.canciones:
            if cancion.nombre.lower() == nombre_cancion.lower():
                print(f"Reproduciendo: {cancion}")
                time.sleep(cancion.duracion)
                return
        print(f"No se encontró la canción '{nombre_cancion}' en la playlist {self.nombre}.")

class Usuario:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.playlists = []  # Lista de playlists del usuario

    def crear_playlist(self, nombre_playlist):
        nueva_playlist = Playlist(nombre_playlist)
        self.playlists.append(nueva_playlist)

    def ver_playlists(self):
        if not self.playlists:
            print(f"{self.nombre_usuario} no tiene playlists.")
        else:
            print(f"Playlists de {self.nombre_usuario}:")
            for idx, playlist in enumerate(self.playlists, 1):
                print(f"{idx}. {playlist.nombre}")

    def agregar_cancion_a_playlist(self, nombre_playlist, cancion):
        for playlist in self.playlists:
            if playlist.nombre.lower() == nombre_playlist.lower():
                # Comprobar si la canción ya existe en la playlist
                existe = False
                for cancion_in_playlist in playlist.canciones:
                    if cancion_in_playlist.nombre.lower() == cancion.nombre.lower():
                        existe = True
                        break
                if not existe:
                    playlist.agregar_cancion(cancion)
                    print(f"Canción {cancion} agregada a la playlist {nombre_playlist}.")
                else:
                    print(f"La canción {cancion} ya está en la playlist {nombre_playlist}.")
                return
        print(f"No se encontró la playlist '{nombre_playlist}'.")

    def reproducir_playlist(self, nombre_playlist):
        for playlist in self.playlists:
            if playlist.nombre.lower() == nombre_playlist.lower():
                playlist.reproducir()
                return
        print(f"No se encontró la playlist '{nombre_playlist}'.")

class SpotifyApp:
    def __init__(self, usuario):
        self.usuario = usuario

    def crear_playlist(self, nombre_playlist):
        self.usuario.crear_playlist(nombre_playlist)

    def ver_playlists(self):
        self.usuario.ver_playlists()

    def agregar_cancion_a_playlist(self, nombre_playlist, cancion):
        self.usuario.agregar_cancion_a_playlist(nombre_playlist, cancion)

    def reproducir_playlist(self, nombre_playlist):
        self.usuario.reproducir_playlist(nombre_playlist)

