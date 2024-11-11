
class Contactos():  #viene por Default en el telefono -> creo instancias de esta clase a través de un atributo en Telefono
    def __init__(self): #crea diccionarios donde se almacenan los contactos, usa los numeros como keys
        self.contactos_guardados= {}

    def agregar_contacto(self, nombre, numero, correo, direccion ):

        """
        Agrega un nuevo contacto a la lista de contactos guardados.

        Parámetros:
        ----------
        nombre : str
            Nombre del contacto a agregar.
        numero : str
            Número de teléfono del contacto.
        correo : str
            Correo electrónico del contacto.
        direccion : str
            Dirección del contacto.

        Lanza:
        ------
        ValueError
            Si el número de teléfono ya existe en los contactos guardados.
        """

        if numero not in self.contactos_guardados.keys():
            self.contactos_guardados[numero] = Contacto(nombre, numero, correo, direccion + '\n')
        else:
            raise ValueError('El contacto ya existe')

    def actualizar_contacto(self, numero, nombre=None, correo=None, direccion=None):
        """
        Actualiza la información de un contacto existente.

        Parámetros:
        ----------
        numero : str
            Número de teléfono del contacto que se desea actualizar.
        nombre : str, opcional
            Nuevo nombre del contacto. Si no se proporciona, no se modifica.
        correo : str, opcional
            Nuevo correo electrónico del contacto. Si no se proporciona, no se modifica.
        direccion : str, opcional
            Nueva dirección del contacto. Si no se proporciona, no se modifica.

        Imprime:
        --------
        Un mensaje indicando si el contacto fue actualizado o si no se encontró el número.
        """

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
class Contacto: #clase teórica
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