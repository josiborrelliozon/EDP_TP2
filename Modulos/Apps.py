class App:
    def __init__(self, id_app):
        self.id_app = id_app

class Contactos(App):
    def __init__(self, nombre, numero, correo, id_app):
        super().__init__(id_app)
        self.nombre = nombre
        self.numero= numero
        self.correo = correo

    def actualizar_contacto(self, nuevo_nombre, nuevo_numero, nuevo_correo):
        self.nombre = nuevo_nombre
        self.numero = nuevo_numero
        self.correo = nuevo_correo

class TelefonoApp(App):
    def __init__(self, id_app):
        super().__init__(id_app)
        self.nombre = Contactos.nombre
        self.numero = Contactos.numero
        'Creo q estas dos lineas no son necesarias pero h'

    'a. Realizar llamadas a otros teléfonos marcando el número..'
    def llamar(self,numero):
        print(f'Estas llamando al {numero}')

    'b. Recibir llamadas de otros números.'
    def atender(self, numero):
        print(f'Te esta llamando el {numero}')

    'c. Terminar una llamada en curso.'
    def cortar_llamada(self,numero):
        print(f'Cortaste la llamada del {numero}')

'e. Enviar y recibir mensajes de texto (SMS) a un número de destino.'
'f. Ver bandeja de entrada de SMS e historial de llamadas.'
'g. Eliminar mensajes (SMS)'
class MesanjesApp(App):
    def __init__(self, id_app):
        super().__init__(id_app)
