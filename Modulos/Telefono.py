class App:
    def __innit__(self, id_app):
        self.id_app = id_app

class Contactos(App):
    def __innit__(self, nombre, numero, correo, id_app):
        super().__init__(id_app)
        self.nombre = nombre
        self.numero= numero
        self.correo = correo

    def actualizar_contacto(self, nuevo_nombre, nuevo_numero, nuevo_correo):
        self.nombre = nuevo_nombre
        self.numero = nuevo_numero
        self.correo = nuevo_correo

#class TelefonoApp:
#    def __innit__(self, ):



class Telefono:
    def __init__(self, id, nombre, modelo, os, version_os, ram, almacenamiento, numero, estado = 0, estado_pan = 0):
        self.id = id # hay q hacerlo unico en central, dentral da los id
        self.nombre = nombre
        self.modelo = modelo
        self.os = os
        self.version_os = version_os
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.numero = numero
        self.estado = estado
        self.estado_pan = estado_pan

    def encenderse(self):
        if self.estado == 0:
            self.estado = 1
        else:
            self.estado = 0

    def desbloquear(self):
        if self.estado ==1:
            if self.estado_pan == 0:
                self.estado_pan = 1
            else:
                self.estado_pan = 0
        else:
            raise Exception("El celular esta apagado")
try:
    mi_telefono = Telefono(2,"jose","nokia","ios",12,8,500,4313)
    print(mi_telefono.estado, mi_telefono.estado_pan)
    mi_telefono.encenderse()
    print(mi_telefono.estado, mi_telefono.estado_pan)
    mi_telefono.desbloquear()
    print(mi_telefono.estado, mi_telefono.estado_pan)
    mi_telefono.encenderse()
    print(mi_telefono.estado, mi_telefono.estado_pan)
    mi_telefono.desbloquear()
    print(mi_telefono.estado, mi_telefono.estado_pan)
except Exception as e:
    print(e)
