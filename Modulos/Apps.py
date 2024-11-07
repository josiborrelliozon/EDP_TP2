from Apps import *
#class MensajesApp():
 #   def __init__(self):

  #  def enviar_mensaje(self, mensaje, numero):
   #     print(f'Enviando mensaje: {mensaje} a numero: {numero}')#e. Enviar y recibir mensajes de texto (SMS) a un número de destino.'


    #def recibir_mensaje(self, mensaje, numero):
     #   print(f'Recibiendo mensaje: {mensaje} de numero: {numero}')#f. Ver bandeja de entrada de SMS e historial de llamadas.'


    #def eliminar_mensaje(self, mensaje):
     #   print(f'Eliminando mensaje: {mensaje}')#g. Eliminar mensajes (SMS)'
#class mailApp(App):
  # def __init__(self, espacio, id_app, nombre_app):
      # super().__innit__(espacio, id_app, nombre_app)
      # self.recibidos = []
      # self.enviados = []

  # def pantalla_de_inicio(self):
     #  for i in range(len(self.recibidos),-1):
         #  print(self.recibidos[i])

from datetime import datetime
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


