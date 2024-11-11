from Contactos import *
from AppStore import *
from Mail import *
from datetime import datetime, timedelta
from Configuracion import *
#from CalculadoraGrafica import *
import numpy as np
from Telefono import *



#En el siguiente archivo, se encuentran las clases: Telefono, TelefonoApp, Central, MensajesApp y SMS (clase abstacta invocada en MensajesApp) y el MAIN


class Central:
    # - Mantener un registro (log) de la información de cada una de las comunicaciones, que será útil para
    # el análisis de datos
    telefonos_registrados = {}  #uso diccionario para que no se repitan los contactos, usando el id como key
    llamadas_en_curso = []
    historico_llamadas = []
    numeros_existentes = []  # registra todos los telefonos instanciados en Telefono
    numeros_conectados_red = []  # registra todos los telefonos disponibles
    numeros_conectados_internet = [] #registra numeros conectados a internet
    id_num = 0

    def __init__(self, nombre): #Creo una Central: ej Claro, Personal, etc
        self.nombre = nombre

    def central_conexion_red(self,numero):
        Central.numeros_conectados_red.append(self.numero)



    @classmethod
    def crear_telefono(cls, nombre, modelo, os, version_os, ram, almacenamiento, numero, espacio_libre=50, estado=0, estado_pantalla=0, estado_red=0, estado_internet=0):
        if numero in Central.numeros_existentes: #se verifica que el número no se repita
            raise ValueError("El numero ingresado ya existe")
        telefono = Telefono(nombre, modelo, os, version_os, ram, almacenamiento, numero, espacio_libre, estado, estado_pantalla, estado_red, estado_internet)
        cls.numeros_existentes.append(numero)
        cls.alta_id(telefono)

    @classmethod
    def alta_id(cls, telefono):  # Cambiamos 'self' por 'cls' para usarlo como método de clase
        if telefono.numero not in cls.numeros_existentes:
            raise ValueError("Este numero no existe")
        else:
            cls.telefonos_registrados[cls.id_num] = telefono
            telefono.id_central = cls.id_num
            cls.id_num += 1

    @classmethod
    def baja_id(cls, telefono):
        if telefono.id_central not in cls.telefonos_registrados:
            raise ValueError("Este numero no se encuentra registrado")
        else:
            id_eliminado = cls.telefonos_registrados.pop(telefono.id_central)
            print(f"{id_eliminado} fue eliminado")


    @staticmethod
    def verificar_numero(numero):
        for telefono in Central.telefonos_registrados.values():
            print(f"Verificando número: {telefono.numero}")
            if telefono.numero == numero:
                print("Número encontrado")
                return True  # Número encontrado
        print("Número no registrado")
        return False  # Número no encontrado

    @staticmethod
    def verificar_red(numero):
        if numero in Central.numeros_conectados_red:
                return True # Número encontrado
        return False # Número no encontrado

    @staticmethod
    def verificar_internet(numero):
        if numero in Central.numeros_conectados_internet:
                return True # Número encontrado
        return False # Número no encontrado



