
from Telefono import *

class App():
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio

class AppStore():

    def __init__(self):
        self.apps_instaladas = {}
        self.apps_disponibles = {} #no instaladas pero existentes, cuando hago spotifyy poner aca

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
        if nombre not in self.apps_instaladas:
            raise ValueError("Esta app no existe")
        valor_eliminado = self.apps_instaladas.pop(nombre)
        print(f'{nombre} borrada con exito')

    @staticmethod
    def hay_espacio(espacio, tamano_app):
        return espacio - tamano_app > 0

    
try:
    if __name__ == '__main__':
        App('spotify',12)
        celu = AppStore()
        celu.instalar_app("spotify")

except ValueError as e:
    print(e)


