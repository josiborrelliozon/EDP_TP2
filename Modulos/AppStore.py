from Apps import *
from Modulos.Spotify import SpotifyApp


class AppStore(): #viene por Default en el telefono -> creo instancias de esta clase a través de un atributo en Telefono

    def __init__(self): #
        self.apps_instaladas = {}
        self.apps_disponibles = {"Spotify": SpotifyApp()} #no instaladas pero existentes, cuando hago spotifyy poner aca



    def instalar_app(self, nombre, espacio):
        if nombre not in self.apps_disponibles.keys():
            raise ValueError("Esta app no existe")    #HACER EXCEPT
        aux = self.apps_disponibles[nombre]
        if self.hay_espacio(espacio,aux.espacio):
            self.apps_disponibles.pop(nombre)
            self.apps_instaladas[nombre] = aux
            print(f'{nombre} instalada con exito')

        else:
            raise ValueError("No hay espacio disponible")


    def borrar_app(self, nombre):
        if nombre not in self.apps_instaladas.keys():
            raise ValueError("Esta app no se encuentra instalada")
        else:
            valor_eliminado = self.apps_instaladas.pop(nombre)
            self.apps_instaladas[nombre] = valor_eliminado
            print(f'{nombre} borrada con exito')

    def hay_espacio(self, espacio_disponible, tamano_app):
        return espacio_disponible >= tamano_app

    
try:
    if __name__ == '__main__':
        App('spotify',12)
        celu = AppStore()
        celu.instalar_app("spotify")
        print("ok")

except ValueError as e:
    print(e)


