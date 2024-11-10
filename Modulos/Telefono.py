from Contactos import *
from AppStore import *
from Llamadas import *
from Central import *
from Mail import *
from MensajesApp import *
from Modulos.CalculadoraGrafica import CalculadoraGrafica
import numpy as np

#Un teléfono celular tiene al menos los siguientes atributos:
#ID (único), Nombre, Modelo, Sistema Operativo y versión, capacidad de memoria RAM, capacidad de
#almacenamiento y número telefónico.

class Telefono:

    numeros_registrados = [] #registra todos los numero creados
    numeros_conectados = [] # registra todos los numeros con conexión a red activada

    def __init__(self,  id_telefono, nombre, modelo, os, version_os, ram, almacenamiento, numero, espacio_libre = 50,  estado = 0, estado_pantalla = 0, estado_red=0): #PONER CONFIGURACION, mensajes_app
        if len(str(numero)) != 8:
            raise ValueError("El numero ingresado es inválido") 
        if numero in Telefono.numeros_registrados: #se verifica que el número no se repita
            raise ValueError("El numero ingresado ya existe")
        if espacio_libre > almacenamiento: #se verifica que el espacio libre no supere al almacenamiento
            raise ValueError("El espacio libre no puede ser mayor al almacenamiento")

        self.id_telefono = id_telefono
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
        self.estado_red = estado_red #modo avion on/off
        self.contactos = Contactos() #viene por default en el telefono
        self.telefono_app = TelefonoApp() #viene por default en el telefono
        self.appstore = AppStore() #viene por default en el telefono
        self.mail_app = mailApp() #viene por default en el telefono
        self.mensajes_app = MensajesApp() #viene por default en el telefono
        self.calculadora_grafica = CalculadoraGrafica()


        Telefono.numeros_registrados.append(self.numero)

    def __str__(self):
        return f'(nombre: {self.nombre}, modelo: {self.modelo} , numero: {self.numero})'

    def __repr__(self):  #se usa para una representación detallada del objeto, ideal para depuración y cuando un objeto se muestra en una lista o diccionari
        return f'(nombre: {self.nombre}, modelo: {self.modelo} , numero: {self.numero})'

    # .........................................Metodos del telefono ..................................................................
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

    #  ....................................Wrappers con metodos de Llamadas..................................................................

    def llamar(self, numero):
        if self.estado_red == 0:
            print("El celular no esta conectado a la red")      #hacer un ValueError!!!!!!!!!!!!!!!
            return

        self.telefono_app.llamar(self.numero, numero)

    def atender(self):
        if self.estado_red == 0 or self.estado == 0:
            raise ValueError("")
        else:
            self.telefono_app.atender()
    #FALTA CORTAR

    #  ....................................Wrappers con metodos de AppStore...............................................................

    def instalar_app(self, nombre):
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0:
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.appstore.instalar_app(nombre, self.espacio_libre)
            print(self.appstore.apps_instaladas)
        #aux = self.appstore.apps_instaladas
        #if nombre in aux:
            #self.espacio_libre -= aux[nombre]
            #print(f'Espacio libre restante {self.espacio_libre}')

    def borrar_app(self, nombre): #borra el app si esta instalada y si el celular esta prendido y desbloqueado
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")
        else:
            self.appstore.borrar_app(nombre, self.espacio_libre)

    #  ....................................Wrappers con metodos de Contactos................................................................

    def nuevo_contacto(self, nombre, numero, correo = None, direccion = None): #agrega un nuevo contacto, verificando que el celular este desbloqueado y prendido
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")
        else:
            self.contactos.agregar_contacto(nombre, numero, correo, direccion)

    def actualizar_contacto(self, numero, nombre, correo = None, direccion = None):
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")

        else:
            self.contactos.actualizar_contacto(numero, correo, direccion)

    #  ....................................Wrappers con metodos de App de Mensajes SMS................................................................

    def enviar_sms(self, numero, mensaje): #envia un SMS verificando que el dispositivo se encuentre conectado a la red
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0:
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.enviar_sms(numero, mensaje)

    def visualizar_entrada(self):  # Devuelve todos los SMS recibidos verificando que el dispositivo se encuentre conectado a la red
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0:
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.visualizar_entrada()

    def cargar_mensaje(self, numero, mensaje, fecha): #Genera mensajes (simula que recibo mensajes)
        if self.estado_red == 0:
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.cargar_mensaje(numero, mensaje, fecha)

    def eliminar_mensaje(self, numero, mensaje, fecha):  # Elimina mensajes recibidos
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0:
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mensajes_app.eliminar_mensaje(numero, mensaje, fecha)

#  ....................................Wrappers con metodos de Mail.................................................

    def cargar_mail(self, fecha_envio, remitente, destinatario, contenido, asunto=None, leido=False):

            self.mail_app.cargar_mail(fecha_envio, remitente, destinatario, contenido, asunto, leido)

    def buzon_mails(self):
        if self.estado == 0:
            raise ValueError("El celular se encuentra apagado")
        elif self.estado_pantalla == 0:
            raise ValueError("El celular se encuentra bloqueado")
        elif self.estado_red == 0:
            raise ValueError("El celular no esta conectado a la red")
        else:
            self.mail_app.buzon_mails()
try:
    if __name__=='__main__':
        telefono_nacho = Telefono(12, "Nacho", "Iphone", "X", "IOS", 20, 500, 12345678, 400 )
        telefono_jose = Telefono(2, "Jose", "Iphone", "X", "IOS", 20, 600, 87654321, 400)
        telefono_agus = Telefono("Agus", "nokia", "cubo", "nok", 8, 500, 100, 11112222, 21)

        telefono_nacho.on_off()
        print(telefono_nacho)
        print(Telefono.numeros_registrados)

        print(".....................Pruebo conexion a red................................")

        telefono_jose.on_off() #prendo telefono
        telefono_jose.conexion_red() #conecto a la red
        print(Telefono.numeros_conectados)
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
        telefono_nacho.mail_app.buzon_mails()

        print("..........................Pruebo Central............................")

        telefono_fede = Telefono("Fede", "nokia", "cubo", "nok", 8, 500, 128, 11113333, 21)
        print(Telefono.numeros_registrados)

        id1 = Central(1)
       # id1.alta_id(telefono_fede)


        print(Central.telefonos_registrados)
        #id1.alta_id(telefono_nacho)  #por que desde Central funciona y aca no


        print("..........................Pruebo Contactos............................")

        telefono_nacho.desbloquear()

        telefono_nacho.nuevo_contacto("Jose Borrelli", 123456789, "jb@itba.edu.ar", "Av Santa Fe 1200")
        telefono_nacho.nuevo_contacto("Jose Sarasqueta", 912201831, "js@itba.edu.ar", "Av Cabildo 1200")
        print(telefono_nacho.contactos)
        telefono_nacho.actualizar_contacto(912201831, "Jose Sarasqueta ITBA" )  #NO ME ACUALIZA EL NOMBRE
        print(telefono_nacho.contactos)

        print("..........................Pruebo AppStore............................")
        #telefono_nacho.instalar_app("spotify") # tengo que vincular app store con spotify

        print("..........................Pruebo Llamada............................")
        # print(telefono_nacho.estado_red) # 0
        # telefono_nacho.llamar(921) #pruebo condicion de conexion a la red
        # telefono_nacho.conexion_red()
        # telefono_nacho.llamar(921) #pruebo condicion de numero valido
        # #veo a que telefono puedo llamar
        # telefono_nacho.llamar(87654321)
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



