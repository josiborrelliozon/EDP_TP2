from Contactos import *
from AppStore import *
from Mail import *
from Central import *

class Telefono:
    id_telefono= 1000
    def __init__(self, nombre, modelo, os, version_os, ram, almacenamiento, numero, espacio_libre = 50,  estado = 0, estado_pantalla = 0,codigo = 0, estado_red=0, estado_internet =0): #PONER CONFIGURACION, mensajes_app
        if len(str(numero)) != 8:
            raise ValueError("El numero ingresado es inválido")

        if espacio_libre > almacenamiento: #se verifica que el espacio libre no supere al almacenamiento
            raise ValueError("El espacio libre no puede ser mayor al almacenamiento")


        self.id_telefono = Telefono.id_telefono
        self.nombre = nombre
        self.codigo = codigo
        self.modelo = modelo
        self.os = os #sistema operativo
        self.version_os = version_os #sistema operativo
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.espacio_libre = espacio_libre
        self.numero = numero
        self.estado = estado  #on/off
        self.estado_pantalla = estado_pantalla #bloqueado/desbloqueado
        self.estado_red = estado_red #conexion a la red para realizar y recibir llamadas
        self. estado_internet = estado_internet #conexion a internet
        self.contactos = Contactos() #viene por default en el telefono
        self.telefono_app = TelefonoApp() #viene por default en el telefono
        self.appstore = AppStore() #viene por default en el telefono
        self.mail_app = mailApp() #viene por default en el telefono
        self.mensajes_app = MensajesApp() #viene por default en el telefono
        self.configuracion = Configuracion()
        #self.calculadora_grafica = CalculadoraGrafica()

        Telefono.id_telefono += 1


    def __str__(self):
        return f'(nombre: {self.nombre}, id_telefono: {self.id_telefono} , numero: {self.numero}, conectado a red: {self.estado_red}, prendido: {self.estado}, conexión internet: {self.estado_internet})'

    def __repr__(self):  #se usa para una representación detallada del objeto, ideal para depuración y cuando un objeto se muestra en una lista o diccionario
        return f'(nombre: {self.nombre}, id_telefono: {self.id_telefono} , numero: {self.numero}, conectado a red: {self.estado_red}, prendido: {self.estado}, conexión internet: {self.estado_internet})'

    # .........................................Metodos del telefono ..................................................................
    def on_off(self):
        if self.estado == 0: #celular apagado, lo prende
            self.estado = 1
            print(f'Prendido: {self}')
        else:                 #celular prendido, lo apaga
            self.estado = 0
            print(f'Apagado {self}')
            if self.estado_red == 1: #cuando apago un celular, se desconecta de la red
                self.conexion_red()
            if self.estado_internet == 1: #cuando apago el celular, se desconecta el internet
                self.conexion_internet()

    def telefono_cambiar_nombre(self, nombre_nuevo):
        Telefono.nombre = nombre_nuevo

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
                print(f" {self.numero} activó conexión a red")
                Central.numeros_conectados_red.append(self.numero)
            else: #si el celular está conectado a una red
                self.estado_red = 0 #lo pone en "modo avión"
                print(f" {self.numero} desactivó conexión a red")
                Central.numeros_conectados_red.remove(self.numero)
        else: #si el celular está apagado
            print(f" {self.numero}: Para conectar a la red debe encender el telefono ")

    def conexion_internet(self):
        if self.estado == 1: #si el celular está prendido
            if self.estado_internet == 0: #y el celular está sin internet
                self.estado_internet = 1 #conecta a internet
                print(f" {self.numero} se conecto a internet")
                Central.numeros_conectados_internet.append(self.numero)
            else: #si el celular está conectado a una red
                self.estado_internet = 0 #lo desconecta de internet
                print(f" {self.numero} desactivó conexión a internet")
                Central.numeros_conectados_internet.remove(self.numero)
        else: #si el celular está apagado
            print(f" {self.numero}: Para conectar a internet debe encender el telefono ")


    #  ....................................Wrappers con metodos de Llamadas..................................................................

    def llamar(self, numero): #llamo a un numero usando App de llamadas
        if self.numero not in Central.numeros_conectados_red: #verifico conexion a red desde Central
            return ValueError("El celular no esta conectado a la red")      #hacer un ValueError!!!!!!!!!!!!!!!

        self.telefono_app.llamar(self.numero, numero)

    def atender(self, numero):
        if self.numero not in Central.numeros_conectados_red:
            raise ValueError("Tu telefono no se encuentra disponible")
        else:
            self.telefono_app.atender(self.numero, numero)

    def cortar(self, numero):
        self.telefono_app.cortar(self.numero, numero)


    #  ....................................Wrappers con metodos de AppStore...............................................................

    def instalar_app(self, nombre):
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_internet == 0: #telefono debe estar conectado a internet
            raise ValueError("El celular no esta conectado a internet")
        else:
            self.espacio_libre -= self.appstore.instalar_app(nombre, self.espacio_libre)
            print(self.appstore.apps_instaladas)
        #aux = self.appstore.apps_instaladas
        #if nombre in aux:
            #self.espacio_libre -= aux[nombre]
            #print(f'Espacio libre restante {self.espacio_libre}')

    def borrar_app(self, nombre): #borra el app si esta instalada y si el celular esta prendido y desbloqueado
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        else:
            self.espacio_libre += self.appstore.borrar_app(nombre, self.espacio_libre)

    #  ....................................Wrappers con metodos de Contactos................................................................

    def nuevo_contacto(self, nombre, numero, correo = None, direccion = None): #agrega un nuevo contacto, verificando que el celular este desbloqueado y prendido
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        else:
            self.contactos.agregar_contacto(nombre, numero, correo, direccion)

    def actualizar_contacto(self, numero, nombre, correo = None, direccion = None):
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")

        else:
            self.contactos.actualizar_contacto(numero, correo, direccion)

    #  ....................................Wrappers con metodos de App de Mensajes SMS................................................................

    def enviar_sms(self, numero, mensaje): #envia un SMS verificando que el dispositivo se encuentre conectado a la red
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.enviar_sms(numero, mensaje)

    def visualizar_entrada(self):  # Devuelve todos los SMS recibidos verificando que el dispositivo se encuentre conectado a la red
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0: #pantalla debe estar conectada red
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.visualizar_entrada()

    def cargar_mensaje(self, numero, mensaje, fecha): #Genera mensajes (simula que recibo mensajes)
        if self.estado_red == 0: #pantalla debe estar conectada red
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.cargar_mensaje(numero, mensaje, fecha)

    def eliminar_mensaje(self, numero, mensaje, fecha):  # Elimina mensajes recibidos
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0: #pantalla debe estar conectada red
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.eliminar_mensaje(numero, mensaje, fecha)

#  ....................................Wrappers con metodos de Mail.................................................

    def cargar_mail(self, fecha_envio, remitente, destinatario, contenido, asunto=None, leido=False):
            self.mail_app.cargar_mail(fecha_envio, remitente, destinatario, contenido, asunto, leido)

    def buzon_mails(self):
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_internet == 0: #pantalla debe estar conectada a internet
            raise ValueError("El celular no esta conectado a internet")
        else:
            self.mail_app.buzon_mails()