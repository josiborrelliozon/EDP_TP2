from Central import *

class Configuracion:
    def __init__(self):
        self.hola = 0
    def configuracion_cambiar_nombre_telefono(self, nuevo_nombre):
        Telefono.telefono_cambiar_nombre(self, nuevo_nombre)
        print(f"Se cambio el nombre del telefono a {Telefono.nombre}")

    def configuracion_cambiar_codigo(self, nuevo_codigo):
        Telefono.codigo = nuevo_codigo
        print(f"Se cambio el codigo del telefono a {Telefono.codigo}")

