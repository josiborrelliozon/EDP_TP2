from Contactos import *
from AppStore import *
from Llamadas import *
from Mail import *
from MensajesApp import *
from Modulos.CalculadoraGrafica import CalculadoraGrafica
import numpy as np
from Spotify import *
class Central:
    # Verificar el estado de los dispositivos que quieren comunicarse.
    # - Verificar los teléfonos que están registrados en la red.
    # - Verificar el estado de los dispositivos que intentan acceder a internet.
    # - Establecer y mediar la comunicación (Ej. dirigir un mensaje al destino, gestionar el estado
    # “ocupado” durante las llamadas, etc.).
    # - Mantener un registro (log) de la información de cada una de las comunicaciones, que será útil para
    # el análisis de datos
    telefonos_registrados = {}  #uso diccionario para que no se repitan los contactos, usando el id como key
    llamadas_en_curso = []
    numeros_existentes = []  # registra todos los telefonos instanciados en Telefono
    numeros_conectados_red = []  # registra todos los telefonos disponibles
    numeros_conectados_internet = [] #registra numeros conectados a internet
    id_num = 0

    def __init__(self, nombre): #Creo una Central: ej Claro, Personal, etc
        self.nombre = nombre


    def alta_id(self, telefono): # Asigno un id a un telefono
        if telefono.numero not in Central.numeros_existentes: #verifico que la instancia del telefon fue creada
            raise ValueError("Este numero no existe")
        else:
            Central.telefonos_registrados[Central.id_num] = telefono
            telefono.id_central = Central.id_num
            Central.id_num += 1
    def baja_id(self, telefono): # Se da de baja un id y se desregistra el telefono
       if telefono.id_central not in Central.telefonos_registrados.keys():
           raise ValueError("Este numero no se encuentra registrado")
       else:
           id_eliminado = Central.telefonos_registrados.pop(telefono.id_central)
           print(f"{id_eliminado} fue eliminado")

    @staticmethod
    def verificar_numero(numero): # Verificar si el número existe en los teléfonos registrados
        for telefono in Central.telefonos_registrados.values():
            if telefono.numero == numero:
                return True  # Número encontrado
        return False  # Número no encontrado

    @staticmethod
    def verificar_red(numero):
        if numero in Central.numeros_conectados_red:
                return True # Número encontrado
        return False # Número no encontrado

    @staticmethod
    def verificar_internet(numero):
        if numero in Central.numeros_conectados_internet:
                return True # Número encontrado
        return False # Número no encontrado


class Telefono:

    def __init__(self,  id_telefono, nombre, modelo, os, version_os, ram, almacenamiento, numero, espacio_libre = 50,  estado = 0, estado_pantalla = 0, estado_red=0, estado_internet =0): #PONER CONFIGURACION, mensajes_app
        if len(str(numero)) != 8:
            raise ValueError("El numero ingresado es inválido") 
        if numero in Central.numeros_existentes: #se verifica que el número no se repita
            raise ValueError("El numero ingresado ya existe")
        if espacio_libre > almacenamiento: #se verifica que el espacio libre no supere al almacenamiento
            raise ValueError("El espacio libre no puede ser mayor al almacenamiento")

        self.id_telefono = id_telefono
        self.id_central = None
        self.nombre = nombre
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
        #self.calculadora_grafica = CalculadoraGrafica()


        Central.numeros_existentes.append(self.numero)

    def __str__(self):
        return f'(nombre: {self.nombre}, modelo: {self.modelo} , numero: {self.numero})'

    def __repr__(self):  #se usa para una representación detallada del objeto, ideal para depuración y cuando un objeto se muestra en una lista o diccionari
        return f'(nombre: {self.nombre}, modelo: {self.modelo} , numero: {self.numero})'

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
            print("El celular no esta conectado a la red")      #hacer un ValueError!!!!!!!!!!!!!!!
            return

        self.telefono_app.llamar(self.numero, numero)

    def atender(self):
        if self.numero not in Central.numeros_conectados_red:
            raise ValueError("Tu telefono no se encuentra disponible")
        else:
            self.telefono_app.atender()
    #FALTA CORTAR

    #  ....................................Wrappers con metodos de AppStore...............................................................

    def instalar_app(self, nombre):
        if self.estado == 0: #telefono debe estar prendido
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0: #pantalla debe estar desbloqueada
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_internet == 0: #telefono debe estar conectado a internet
            raise ValueError("El celular no esta conectado a internet")
        else:
            self.appstore.instalar_app(nombre, self.espacio_libre)
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
            self.appstore.borrar_app(nombre, self.espacio_libre)

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
try:
    if __name__=='__main__':
        telefono_nacho = Telefono(12, "Nacho", "Iphone", "X", "IOS", 20, 500, 12345678, 400 )
        telefono_jose = Telefono(2, "Jose", "Iphone", "X", "IOS", 20, 600, 87654321, 400)
        telefono_agus = Telefono(5, "Agus", "Nokia", "nok", 8, 500, 100, 11112222, 21)
        telefono_fede = Telefono(123, "Telefono de Fede", "cubo", "nok", 8, 500, 123, 11113333, 21)
        telefono_pedro = Telefono(12, "Telefono de Pedro", "cubo", "nok", 8, 500, 123, 11110000, 21)
        telefono_nacho.on_off()
        telefono_nacho.desbloquear()
        telefono_nacho.conexion_internet()
        telefono_nacho.conexion_red()
        print(telefono_nacho)
        print(Central.numeros_existentes)

        print(".....................Pruebo conexion a red................................")

        telefono_jose.on_off() #prendo telefono
        telefono_jose.conexion_red() #conecto a la red
        print(Central.numeros_conectados_red)
        print(telefono_nacho.estado_red)

        print("..........................Pruebo Mail............................")

        #cargo los mails
        telefono_nacho.mail_app.cargar_mail(datetime(2024, 10, 10, 1), "agus@gmail.com", "nacho@gmail.com",
                              "Estamos muy complicados con el TP. Que hacemos?", "TP Estructuras", True)
        telefono_nacho.mail_app.cargar_mail(datetime(2024, 11, 7, 12), "jose@gmail.com", "nacho@gmail.com",
                              "Hay que pedirle ayuda a Fede. Abrazo.", "RE: TP Estructuras")
        telefono_nacho.mail_app.cargar_mail(datetime(2023, 11, 7, 12), "jose@gmail.com", "nacho@gmail.com",
                              "Adjunto a continuacion la tabla de datos", "Parcial de Quimica")
        telefono_nacho.mail_app.cargar_mail(datetime.now() - timedelta(days=1), "pedro@hotmail", "nacho@gmail.com",
                              "te invitamos al partido del sabado", "Partido Sabado")
        telefono_nacho.mail_app.cargar_mail(datetime.now() - timedelta(days=1), "luis@itba.edu.ar", "nacho@gmail.com",
                              "La presentacion es el jueves, tenemos que tener el pwp preparado. Te adjunto los avances.",
                              "TP Estructuras", True)

        #Muestra buzon con mails cargados, ordenados por llegada reciente y apareciendo primero los no leidos
        telefono_nacho.buzon_mails()



        print("..........................Pruebo Central............................")
        claro = Central("Claro")

        print(Central.numeros_existentes)
        claro.alta_id(telefono_fede)
        claro.alta_id(telefono_pedro)
        claro.alta_id(telefono_nacho)
        claro.alta_id(telefono_jose)
        claro.alta_id(telefono_agus)

        print(Central.telefonos_registrados)

        claro.baja_id(telefono_fede)
        print(Central.telefonos_registrados)


        print("..........................Pruebo Contactos............................")

        telefono_nacho.nuevo_contacto("Jose Borrelli", 123456789, "jb@itba.edu.ar", "Av Santa Fe 1200")
        telefono_nacho.nuevo_contacto("Jose Sarasqueta", 912201831, "js@itba.edu.ar", "Av Cabildo 1200")
        print(telefono_nacho.contactos)
        telefono_nacho.actualizar_contacto(912201831, "Jose Sarasqueta ITBA" )  #NO ME ACUALIZA EL NOMBRE
        print(telefono_nacho.contactos)

        print("..........................Pruebo AppStore............................")

        telefono_nacho.calculadora_grafica = CalculadoraGrafica()
        telefono_nacho.calculadora_grafica.factorial(5)        
        #telefono_nacho.instalar_app("spotify") # tengo que vincular app store con spotify

        print("..........................Pruebo Llamada............................")
        print(Central.telefonos_registrados)
        print(Central.verificar_numero(11110000))
        #telefono_fede.llamar(1213) #pruebo condicion de conexion a red
        #telefono_nacho.llamar(12) #pruebo condicion de no existencia
        telefono_nacho.llamar(11110000)

        telefono_nacho.llamar(87654321) #pruebo condicion de conexion a la red
        telefono_nacho.conexion_red()
        telefono_nacho.llamar(921) #pruebo condicion de numero valido
        #veo a que telefono puedo llamar
        telefono_nacho.llamar(87654321)
        # print(Central.telefonos_registrados)

        print("........................Pruebo Mensajes APP SMS............................")


        print("..........................Pruebo Calculadora............................")
        telefono_nacho.calculadora_grafica.calcular_polinomios('x**2 - 2*x + 1', 3000)
        telefono_fede.calculadora_grafica.factorial(5)
        telefono_agus.calculadora_grafica.normal(np.random.normal(loc=0, scale=1, size=1000))#genero data sets random
        telefono_jose.calculadora_grafica.desvio([27,25,42,88,15,22,21,15,24,63,73,42,23,12,10,21,21,21,2,12,12,1,21,21,21])



except Exception as e:
    print(e)

except ValueError as e:
    print(e)


