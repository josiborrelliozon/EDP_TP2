
class Telefono:

    numeros_registrados = []
    numeros_conectados = []

    def __init__(self, id_telefono, nombre, modelo, os, version_os, ram, almacenamiento, numero, estado = 0, estado_pantalla = 0, estado_red=0):
        if len(str(numero)) != 8:
            raise ValueError("El numero ingresado es inválido") #a nacho no le funciono pero ahora si
        self.id_telefono = id_telefono
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

    def __str__(self):
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

    def conexion_red(self):
        if self.estado == 1: #si esta prendido
            if self.estado_red == 0:
                self.estado_red = 1
                print(f" {self.numero} activó conexión")
                Telefono.numeros_conectados.append(self.numero)
            else:
                self.estado_red = 0
                print(f" {self.numero} desactivó conexión")
                Telefono.numeros_conectados.remove(self.numero)

        else:
            print(f" {self.numero}: Para conectar a la red debe encenderse el telefono ")


try:
    if __name__=='__main__':
        telefono_nacho = Telefono("Nacho", "nokia", "ios", 12, 8, 500, 12345678)
        mi_telefono = Telefono(2, "jose", "nokia", "ios", 12, 8, 87654321)
        print(telefono_nacho)
        print(Telefono.numeros_registrados)
        mi_telefono.on_off()

        mi_telefono.conexion_red()
        telefono_nacho.conexion_red()
        print(Telefono.numeros_conectados)



except Exception as e:
    print(e)

except ValueError as e:
    print(e)



