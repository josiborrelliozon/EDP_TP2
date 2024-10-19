from Telefono import *
class Central:
    telefonos_registrados = {}

    # Creo los ids desde la central
    def __init__(self, id_telefono):
        if id_telefono in self.telefonos_registrados:
            raise ValueError("Id ya existente")
        self.id_telefono = id_telefono

    # Asigno un id a un telefono
    def alta_id(self, telefono: Telefono):
        if telefono.numero not in Telefono.numeros_registrados:
            raise ValueError("Este numero no existe")
        Central.telefonos_registrados[self.id_telefono] = telefono

    def baja_id(selfself, telefono: Telefono):

try:
    if __name__ == '__main__':
        telefono_nacho = Telefono("Nacho", "nokia", "ios", 12, 8, 500, 12345678)
        print(Telefono.numeros_registrados)
        id1 = Central(1)
        id1.alta_id(telefono_nacho)
        print(Central.telefonos_registrados)

except ValueError as e:
   print(e)









