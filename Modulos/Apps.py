from Telefono import *
from datetime import datetime
from collections import deque

#hacer app de batalla naval


class TelefonoApp():
    def __init__(self, ):
        self.nombre = Contactos.nombre
        self.numero = Contactos.numero
        'Creo q estas dos lineas no son necesarias pero h'

    'a. Realizar llamadas a otros teléfonos marcando el número..'
    def llamar(self,numero: Telefono):
        if numero not in Telefono.telefonos_registrados:
            raise ValueError('Numero inexiste')
        elif numero not in Telefono.numeros_conectados:
            raise ValueError('Número fuera de servicio')
        print(f'Estas llamando al {numero}')

    'b. Recibir llamadas de otros números.'
    def atender(self, numero):
        print(f'Te esta llamando el {numero}')

    'c. Terminar una llamada en curso.'
    def cortar_llamada(self,numero):
        print(f'Cortaste la llamada del {numero}')


#class MensajesApp():
 #   def __init__(self):

  #  def enviar_mensaje(self, mensaje, numero):
   #     print(f'Enviando mensaje: {mensaje} a numero: {numero}')#e. Enviar y recibir mensajes de texto (SMS) a un número de destino.'


    #def recibir_mensaje(self, mensaje, numero):
     #   print(f'Recibiendo mensaje: {mensaje} de numero: {numero}')#f. Ver bandeja de entrada de SMS e historial de llamadas.'


    #def eliminar_mensaje(self, mensaje):
     #   print(f'Eliminando mensaje: {mensaje}')#g. Eliminar mensajes (SMS)'
class mailApp(App):
   def __init__(self, espacio, id_app, nombre_app):
       super().__innit__(espacio, id_app, nombre_app)
       self.recibidos = []
       self.enviados = []

   def pantalla_de_inicio(self):
       for i in range(len(self.recibidos),-1):
           print(self.recibidos[i])


class Email():
    def __init__(self, mail_id, remitente, destinatario, asunto, contenido):
        self.mail.id = mail_id
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.fecha = datetime.now()
        self.leido = False

    def marcar_como_leido(self):
        self.leido = True

    def obtener_info(self):
        return f"Asunto: {self.asunto}, De: {self.remitente}, Para: {self.destinatario}, Fecha: {self.fecha}, Leído: {self.leido}"


#try:
 #   if __name__ == '__main__':
  #      mi_telefono = Telefono(2, "jose", "nokia", "ios", 12, 8, 87654321)
   #     JoseFranciscoITBA = Contactos("Jose Francisco ITBA",  87654321, "jsarasqueta@hotmail.com")

#except ValueError as e:
 #   print(e)


