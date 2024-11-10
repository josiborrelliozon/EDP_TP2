'''Enviar y recibir mensajes de texto (SMS) a un número de destino.
f. Ver bandeja de entrada de SMS e historial de llamadas.
g. Eliminar mensajes (SMS).'''


from Central import *

diccionario = {1: 12345678}

class MensajesApp(): #viene por Default en el telefono -> creo instancias de esta clase a través de un atributo en Telefono
    def __init__(self):
        self.sms_recibidos = []
        self.sms_enviados = []

    def enviar_sms(self, numero, mensaje):
        if numero not in diccionario.values(): #Central.telefonos_registrados.values():
            raise ValueError('Número no registrado')
        else:
            aux = SMS(numero, mensaje, datetime.now())
            self.sms_enviados.append(aux)
            print('Mensaje enviado')
            print(aux)

    def cargar_mensaje(self, numero, mensaje, fecha): #Genera mensajes (simula que recibo mensajes)
        aux = SMS(numero, mensaje, fecha)
        self.sms_recibidos.append(aux)
        print(f'Mensaje recibido de {numero}')

    def visualizar_entrada(self): #Devuelve todos los SMS recibidos
        recibidos = sorted(self.sms_recibidos, key=lambda x: x.fecha_envio, reverse=True)
        print("Bandeja de entrada SMS:")
        for sms in recibidos:
            print(sms)

    def eliminar_mensaje(self, numero, mensaje, fecha):  # Elimina mensajes recibidos
        mensaje_a_eliminar = None
        for sms in self.sms_recibidos:
            if sms.numero == numero and sms.mensaje == mensaje and sms.fecha_envio == fecha:
                mensaje_a_eliminar = sms
                break

        if mensaje_a_eliminar:
            self.sms_recibidos.remove(mensaje_a_eliminar)
            print("Mensaje eliminado")
        else:
            raise ValueError("Mensaje no existente")




class SMS: #Clase abstacta
    def __init__(self, numero, mensaje, fecha_envio):
        self.numero = numero
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio

    def __str__(self):
        fecha_formateada = self.fecha_envio.strftime("%b %d %H:%M")
        return f'{self.numero} ({fecha_formateada}): {self.mensaje} '


try:
    if __name__ == '__main__':
        telefono_nacho = MensajesApp()
        telefono_nacho.cargar_mensaje(11112222, 'Hoy no puedo :(', datetime(2024,2,3,11))
        telefono_nacho.cargar_mensaje(34345656, 'No me sale estooo', datetime(2024,11,3,12))
        telefono_nacho.cargar_mensaje(34345656, 'Buenas tardes', datetime(2024, 10, 13, 12))
        telefono_nacho.enviar_sms(12345678, "Hola como estas")
        telefono_nacho.visualizar_entrada()
        telefono_nacho.eliminar_mensaje(11112222, 'Hoy no puedo :(', datetime(2024,2,3,11))
        telefono_nacho.visualizar_entrada()

except ValueError as error:
    print(error)
