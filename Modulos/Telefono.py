#from TP.EDP_TP2.Modulos.Apps import AppStore
from EDP_TP2.Modulos.Apps import *



#Un teléfono celular tiene al menos los siguientes atributos:
#ID (único), Nombre, Modelo, Sistema Operativo y versión, capacidad de memoria RAM, capacidad de
#almacenamiento y número telefónico.
class Telefono:

    numeros_registrados = []
    numeros_conectados = []

    def __init__(self,  id_telefono, nombre, modelo, os, version_os, ram, almacenamiento, numero, espacio_libre, estado = 0, estado_pantalla = 0, estado_red=0): #PONER CONFIGURACION, mensajes_app
        if len(str(numero)) != 8:
            raise ValueError("El numero ingresado es inválido") #a nacho no le funciono pero ahora si
        if espacio_libre > almacenamiento:
            raise ValueError("Espacio libre debe ser menor al almacenamiento")
        self.id_telefono = id_telefono
        self.nombre = nombre
        self.modelo = modelo
        self.os = os #sistema operativo
        self.version_os = version_os #sistema operativo
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.espacio_libre = espacio_libre
        self.numero = numero
        self.estado = estado
        self.estado_pantalla = estado_pantalla
        self.estado_red = estado_red
        self.contactos = Contactos()
        self.telefono_app = Telefono()
        self.appstore = AppStore()


        Telefono.numeros_registrados.append(self.numero)


    def __str__(self):
        return f'(nombre: {self.nombre}, modelo: {self.modelo} , numero: {self.numero})'

    def on_off(self):
        if self.estado == 0:
            self.estado = 1
            print(f'Prendido: {self}')   #si está prendido, lo apaga. Si está apagado, lo prende
        else:
            self.estado = 0
            print(f'Apagado {self}')

    def desbloquear(self):
        if self.estado ==1: #si el celular está prendido,
            if self.estado_pantalla == 0: #si está bloqueado
                self.estado_pantalla = 1 #lo desbloquea
                print(f'Pantalla desbloqueada: {self}')
            else: #si está desbloqueado,
                self.estado_pantalla = 0 #lo bloquea
                print(f'Pantalla bloqueada: {self}')
        else: #si está apagado,
            raise Exception("El celular se encuentra apagado") #cambiar esto (ta bien, no tiene mucho sentido)

    def conexion_red(self):
        if self.estado == 1: #si el celular está prendido
            if self.estado_red == 0: #y el celular está en "modo avíon"
                self.estado_red = 1 #conecta la red
                print(f" {self.numero} activó conexión")
                Telefono.numeros_conectados.append(self.numero)
            else: #si el celular está conectado a una red
                self.estado_red = 0 #lo pone en "modo avión"
                print(f" {self.numero} desactivó conexión")
                Telefono.numeros_conectados.remove(self.numero)

        else: #si el celular está apagado
            print(f" {self.numero}: Para conectar a la red debe encenderse el telefono ")

class Contacto():
    def __init__(self, nombre, numero, correo ):
        self.nombre = nombre
        self.numero= numero
        self.correo = correo

    def actualizar_contacto(self, nuevo_nombre, nuevo_numero, nuevo_correo):
        self.nombre = nuevo_nombre
        self.numero = nuevo_numero
        self.correo = nuevo_correo
try:
    if __name__=='__main__':
        telefono_nacho = Telefono(12, "Nacho", "Iphone", "X", "IOS", 20, 500, 12345678, 400 )
        mi_telefono = Telefono(2, "Jose", "Iphone", "X", "IOS", 20, 600, 87654321, 400)
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



