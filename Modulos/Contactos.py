
# cada telefono tiene su diccionario de contactos creado en:
class Contactos():
    def __init__(self):
        self.contactos_guardados= {}

    def agregar_contacto(self, nombre, numero, correo, direccion ):
        if numero not in self.contactos_guardados.keys():
            self.contactos_guardados[numero] = Contacto(nombre, numero, correo, direccion + '\n')
        else:
            raise ValueError('El contacto ya existe')

    def actualizar_contacto(self, numero, nombre=None, correo=None, direccion=None):
        if numero in self.contactos_guardados.keys(): #checkea que el numero del contacto que quiero modificar existe
            contacto = self.contactos_guardados[numero]
            if nombre:
                contacto.nombre = nombre
            if correo:
                contacto.correo = correo
            if direccion:
                contacto.direccion = direccion
            print(f"Contacto con numero {numero} actualizado.")
        else:
            print(f"No se encontró un contacto con el numero {numero}.")

    def __str__(self):
        return f'Info de contactos: ({self.contactos_guardados})'

# atributos que debe tener un contacto
class Contacto:
    def __init__(self, nombre, numero, correo = None, direccion = None):  #direccion y correo son opcionales
        self.nombre = nombre
        self.numero = numero
        self.correo = correo
        self.direccion = direccion


    def __repr__(self): #str no me funciona, me tira dxn de memoria
        return f'Nombre: {self.nombre}, Numero: {self.numero}, Correo: {self.correo}, Direccion: {self.direccion} '


if __name__ == '__main__':
    contactos = Contactos()
    contactos.agregar_contacto("Juan Perez", "12345678", "juan@example.com", "Av Las Heras")
    contactos.agregar_contacto("Jose S", "98765432", "juan@example.com", "Av Las Heras")
    print(contactos.contactos_guardados)
    contactos.actualizar_contacto("12345678", "Johnny", "<EMAIL>")
    print(contactos.contactos_guardados)