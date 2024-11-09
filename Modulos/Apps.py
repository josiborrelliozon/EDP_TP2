import locale

locale.setlocale(locale.LC_TIME, 'es_ES')  #me pone las fechas relativas a Espana
from datetime import datetime, timedelta

class mailApp():
   def __init__(self):
      self.recibidos = []

   #Uso el metodo cargar mail solo para crear los mails recibidos
   def cargar_mail(self, fecha_envio, remitente, destinatario, contenido, asunto = None, leido = False ):
       mail = Email(fecha_envio, remitente, destinatario, contenido, asunto, leido)
       self.recibidos.append(mail)

   def buzon_mails(self):
          # Ordeno los emails por fecha_recibido de más reciente a más antiguo
        emails_ordenados = sorted(self.recibidos, key=lambda email: email.fecha_envio, reverse=True)
        for email in emails_ordenados:
            print(email)


from datetime import datetime
class Email():
    def __init__(self, fecha_envio, remitente, destinatario, contenido, asunto = None, leido = False):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.fecha_envio = fecha_envio
        self.leido = False

        # Formato de fecha directamente al inicializar
        dia_semana = self.fecha_envio.strftime("%a")
        fecha = self.fecha_envio.strftime("%d %b")
        hora = self.fecha_envio.strftime("%H:%M")
        tiempo_transcurrido = self.calcular_tiempo_transcurrido()

        self.fecha = f"{dia_semana}, {fecha}, {hora} ({tiempo_transcurrido})"

    def calcular_tiempo_transcurrido(self):
        ahora = datetime.now()
        diferencia = ahora - self.fecha_envio

        # Veo cuantos dias pasaron
        if diferencia.days > 1:
            return f"hace {diferencia.days} días"

        elif diferencia.days == 1:
            return "hace 1 día"

    def __str__(self): #uso repr porque los mails van a a parecer en la lista recibidos y enviados
        if self.leido:
            estado = 'Leído'
        else:
            estado = 'No leído'
        return (f'({self.fecha})  ({estado})  {self.remitente} -> {self.destinatario}. Asunto: {self.asunto}.'
                f'           {self.contenido} ')

    def __repr__(self): #uso repr porque los mails van a a parecer en la lista recibidos y enviados
        if self.leido:
            estado = 'Leído'
        else:
            estado = 'No leído'
        return (f'({self.fecha})  ({estado})  {self.remitente} -> {self.destinatario}. Asunto: {self.asunto}.'
                f'           {self.contenido} ')


if __name__ == '__main__':
    nachomail = mailApp()
    nachomail.cargar_mail(datetime(2024,10, 10, 1),"agus@gmail.com", "nacho@gmail.com", "Estamos muy complicados con el TP. Que hacemos?", "TP Estructuras")
    nachomail.cargar_mail(datetime(2024,11,7, 12),"jose@gmail.com", "nacho@gmail.com", "Hay que pedirle ayuda a Fede. Abrazo.", "RE: TP Estructuras" )
    nachomail.cargar_mail(datetime(2023, 11, 7, 12), "jose@gmail.com", "nacho@gmail.com","Adjunto a continuacion la tabla de datos", "Parcial de Quimica")
    nachomail.cargar_mail(datetime.now()- timedelta(days=1), "pedro@hotmail", "nacho@gmail.com", "te invitamos al partido del sabado", "Partido Sabado")
    nachomail.buzon_mails()


