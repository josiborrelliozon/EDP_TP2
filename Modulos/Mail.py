import locale

locale.setlocale(locale.LC_TIME, 'es_ES')  #me pone las fechas relativas a Espana
from datetime import datetime, timedelta


class mailApp():  #viene por Default en el telefono -> creo instancias de esta clase a través de un atributo en Telefono
    def __init__(self):
        self.noleidos = []
        self.leidos = []

    def cargar_mail(self, fecha_envio, remitente, destinatario, contenido, asunto=None, leido=False):
        mail = Email(fecha_envio, remitente, destinatario, contenido, asunto, leido)
        if not mail.leido:
            self.noleidos.append(mail)
        else:
            self.leidos.append(mail)

    def buzon_mails(self):
        # Ordenar los emails no leídos y leídos por fecha de más reciente a más antigua
        noleidos_ordenados = sorted(self.noleidos, key=lambda email: email.fecha_envio, reverse=True)
        leidos_ordenados = sorted(self.leidos, key=lambda email: email.fecha_envio, reverse=True)

        print("Correos No Leídos:")
        for email in noleidos_ordenados:
            print(email)

        print("\nCorreos Leídos:")
        for email in leidos_ordenados:
            print(email)


from datetime import datetime
class Email():
    def __init__(self, fecha_envio, remitente, destinatario, contenido, asunto = None, leido = False):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.fecha_envio = fecha_envio
        self.leido = leido

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
    nachomail.cargar_mail(datetime(2024,10, 10, 1),"agus@gmail.com", "nacho@gmail.com", "Estamos muy complicados con el TP. Que hacemos?", "TP Estructuras", True)
    nachomail.cargar_mail(datetime(2024,11,7, 12),"jose@gmail.com", "nacho@gmail.com", "Hay que pedirle ayuda a Fede. Abrazo.", "RE: TP Estructuras" )
    nachomail.cargar_mail(datetime(2023, 11, 7, 12), "jose@gmail.com", "nacho@gmail.com","Adjunto a continuacion la tabla de datos", "Parcial de Quimica")
    nachomail.cargar_mail(datetime.now()- timedelta(days=1), "pedro@hotmail", "nacho@gmail.com", "te invitamos al partido del sabado", "Partido Sabado")
    nachomail.cargar_mail(datetime.now() - timedelta(days=1), "luis@itba.edu.ar", "nacho@gmail.com",
                          "La presentacion es el jueves, tenemos que tener el pwp preparado. Te adjunto los avances.", "TP Estructuras", True)
    nachomail.buzon_mails()




