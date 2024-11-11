from Telefono_Central import *
# Verificar el estado de los dispositivos que quieren comunicarse.
# - Verificar los teléfonos que están registrados en la red.
# - Verificar el estado de los dispositivos que intentan acceder a internet.
# - Establecer y mediar la comunicación (Ej. dirigir un mensaje al destino, gestionar el estado
# “ocupado” durante las llamadas, etc.).
# - Mantener un registro (log) de la información de cada una de las comunicaciones, que será útil para
# el análisis de datos

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


    #def baja_id(self): # Se da de baja un id y se desregistra el telefono
      #  if self.id_telefono not in Central.telefonos_existentes.keys():
       #     raise ValueError("Este numero no se encuentra registrado")
        #id_eliminado = Central.telefonos_registrados.pop(self.id_telefono)
        #print(f"{id_eliminado} fue eliminado")



try:
    if __name__ == '__main__':
        claro = Central("Claro")
        telefono_fede = Telefono(123, "Telefono de Fede", "cubo", "nok", 8, 500, 123, 11113333, 21)

        print(Central.numeros_existentes)
        claro.alta_id(telefono_fede)

except ValueError as e:
   print(e)









