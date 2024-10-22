from Telefono import *
class App:
    def __init__(self, id_app, espacio, nombre_app):
        self.id_app = id_app
        self.espacio = espacio
        self.nombre = nombre_app


class AppStore():
    apps_instaladas = {}                         #aca poner todas las apps que vienen por default

    @staticmethod
    def espacio_actual():


    def __init__(self, id_app, nombre_app, numero: Telefono): #verificar que hay espacio en el celular

        self.id_user = numero
        self.id_app = id_app
        self.nombre_app = nombre_app

        AppStore.apps_instaladas[self.id_app] = self

    def borrar_app(self, id_app):                                       #poner condicion que las apps default no se borren
        app_borrada = AppStore.apps_instaladas.pop(self.id_app)
        print(f'{app_borrada} fue eliminada')

class Contactos():
    contactos_guardados ={}
    def __init__(self, nombre, numero, correo):
        if numero not in Telefono.numeros_registrados:
            raise ValueError("El telefono guardado no existe")
        super().__init__()
        self.nombre = nombre
        self.numero= numero
        self.correo = correo
        Contactos.contactos_guardados[self.nombre] = self

    def actualizar_contacto(self, nuevo_nombre, nuevo_numero, nuevo_correo):
        self.nombre = nuevo_nombre
        self.numero = nuevo_numero
        self.correo = nuevo_correo

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


class MensajesApp():
    def __init__(self):

    def enviar_mensaje(self, mensaje, numero):
        print(f'Enviando mensaje: {mensaje} a numero: {numero}')#e. Enviar y recibir mensajes de texto (SMS) a un número de destino.'


    def recibir_mensaje(self, mensaje, numero):
        print(f'Recibiendo mensaje: {mensaje} de numero: {numero}')#f. Ver bandeja de entrada de SMS e historial de llamadas.'


    def eliminar_mensaje(self, mensaje):
        print(f'Eliminando mensaje: {mensaje}')#g. Eliminar mensajes (SMS)'


try:
    if __name__ == '__main__':
        mi_telefono = Telefono(2, "jose", "nokia", "ios", 12, 8, 87654321)
        JoseFranciscoITBA = Contactos("Jose Francisco ITBA",  87654321, "jsarasqueta@hotmail.com")
