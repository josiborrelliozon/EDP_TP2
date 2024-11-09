from Telefono import *

class Central:
    telefonos_registrados = {}
    llamadas_en_curso = []

    # Creo los ids desde la central
    def __init__(self, id_telefono):
        if id_telefono in self.telefonos_registrados:
            raise ValueError("Id ya existente")
        self.id_telefono = id_telefono

    # Asigno un id a un telefono
    def alta_id(self, telefono):
        if telefono.numero not in Telefono.numeros_registrados:
            raise ValueError("Este numero no existe")
        Central.telefonos_registrados[self.id_telefono] = telefono

    def baja_id(self, telefono):
        if telefono.numero not in Telefono.numeros_registrados:
            raise ValueError("Este numero no existe")
        id_eliminado = Central.telefonos_registrados.pop(self.id_telefono)
        print(f"{id_eliminado} fue eliminado")



try:
    if __name__ == '__main__':
        telefono_nacho = Telefono("Nacho", "nokia", "cubo", "nok", 8, 500, 12345678, 12345678, 21)
        print(Telefono.numeros_registrados)
        id1 = Central(1)
        id1.alta_id(telefono_nacho)
        print(Central.telefonos_registrados)
        id1.baja_id(telefono_nacho)
        print(Central.telefonos_registrados)

except ValueError as e:
   print(e)









