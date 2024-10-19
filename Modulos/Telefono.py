
class Telefono:

    numeros_registrados = []

    def __init__(self, nombre, modelo, os, version_os, ram, almacenamiento, numero, estado = 0, estado_pantalla = 0, estado_red=0):
        #if len(str(numero)) != 8:
         #   raise ValueError("El numero ingresado es inválido")

        self.nombre = nombre
        self.modelo = modelo
        self.os = os
        self.version_os = version_os
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.numero = numero
        self.estado = estado
        self.estado_pantalla = estado_pantalla
        self.estado_red = estado_red
        Telefono.numeros_registrados.append(self.numero)

    def __repr__(self):
        return f'(nombre: {self.nombre}, modelo: {self.modelo} , numero: {self.numero})'

    def on_off(self):
        if self.estado == 0:
            self.estado = 1
            print(f'Prendido: {self}')
        else:
            self.estado = 0
            print(f'Apagado {self}')

    def desbloquear(self):
        if self.estado ==1:
            if self.estado_pantalla == 0:
                self.estado_pantalla = 1
                print(f'Pantalla desbloqueada: {self}')
            else:
                self.estado_pantalla = 0
                print(f'Pantalla bloqueada: {self}')
        else:
            raise Exception("El celular se encuentra apagado")


#creo las instancias de telefonos



try:
    if __name__=='__main__':
        telefono_nacho = Telefono("Nacho", "nokia", "ios", 12, 8, 500, 12345678)
        mi_telefono = Telefono(2, "jose", "nokia", "ios", 12, 8, 500, 43131234)

        print(Telefono.numeros_registrados)
        mi_telefono.on_off()

        mi_telefono.desbloquear()

        mi_telefono.on_off()

        mi_telefono.desbloquear()

except Exception as e:
    print(e)

except ValueError as e:
    print(e)


