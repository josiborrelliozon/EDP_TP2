class Telefono:

    def __init__(self,  id_telefono, nombre, modelo, os, version_os, ram, almacenamiento, numero, espacio_libre = 50,  estado = 0, estado_pantalla = 0, estado_red=0, estado_internet =0): #PONER CONFIGURACION, mensajes_app
        if len(str(numero)) != 8:
            raise ValueError("El numero ingresado es inválido")
        if numero in Central.numeros_existentes: #se verifica que el número no se repita
            raise ValueError("El numero ingresado ya existe")
        if espacio_libre > almacenamiento: #se verifica que el espacio libre no supere al almacenamiento
            raise ValueError("El espacio libre no puede ser mayor al almacenamiento")

        self.id_telefono = id_telefono
        self.id_central = None
        self.nombre = nombre
        self.modelo = modelo
        self.os = os #sistema operativo
        self.version_os = version_os #sistema operativo
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.espacio_libre = espacio_libre
        self.numero = numero
        self.estado = estado  #on/off
        self.estado_pantalla = estado_pantalla #bloqueado/desbloqueado
        self.estado_red = estado_red #conexion a la red para realizar y recibir llamadas
        self. estado_internet = estado_internet #conexion a internet
        Central.numeros_existentes.append(self.numero)

    def __str__(self):
        return f'(nombre: {self.nombre}, id_telefono {self.id_telefono} , numero: {self.numero})'

    def __repr__(self):  #se usa para una representación detallada del objeto, ideal para depuración y cuando un objeto se muestra en una lista o diccionari
        return f'(nombre: {self.nombre}, id_telefono {self.id_telefono} , numero: {self.numero})'

class Central:
    telefonos_registrados = {}  #uso diccionario para que no se repitan los contactos, usando el id como key
    llamadas_en_curso = []
    numeros_existentes = []  # registra todos los telefonos instanciados en Telefono
    numeros_conectados_red = []  # registra todos los telefonos disponibles
    numeros_conectados_internet = [] #registra numeros conectados a internet
    id_num = 0

    def __init__(self, nombre): #Creo una Central: ej Claro, Personal, etc
        self.nombre = nombre


    def alta_id(self, telefono): # Asigno un id creado previamente a un telefono
        if telefono.numero not in Central.numeros_existentes:
            raise ValueError("Este numero no existe")
        else:
            Central.telefonos_registrados[Central.id_num] = telefono #VER QUE SEA EL OBJETO
            telefono.id_central = Central.id_num
            Central.id_num += 1
    def baja_id(self, telefono): # Se da de baja un id y se desregistra el telefono
       if telefono.id_central not in Central.telefonos_registrados.keys():
           raise ValueError("Este numero no se encuentra registrado")
       else:
           id_eliminado = Central.telefonos_registrados.pop(telefono.id_central)
           print(f"{id_eliminado} fue eliminado")

    @staticmethod
    def verificar_numero(numero): # Verificar si el número existe en los teléfonos registrados
        for telefono in Central.telefonos_registrados.values():
            if telefono.numero == numero:
                return True  # Número encontrado
        return False  # Número no encontrado

    @staticmethod
    def verificar_red(numero):
        for telefono in Central.numeros_conectados_red:
            if telefono.numero == numero:
                return True # Número encontrado
        return False # Número no encontrado


try:
    if __name__ == '__main__':
        claro = Central("Claro")
        telefono_fede = Telefono(123, "Telefono de Fede", "cubo", "nok", 8, 500, 123, 11113333, 21)
        telefono_pedro =  Telefono(12, "Telefono de Fede", "cubo", "nok", 8, 500, 123, 11112222, 21)
        print(Central.numeros_existentes)
        claro.alta_id(telefono_fede)
        claro.alta_id(telefono_pedro)
        print(Central.telefonos_registrados)
        print( Central.verificar_numero(11113333))

        claro.baja_id(telefono_fede)
        print(Central.telefonos_registrados)



except ValueError as e:
   print(e)
