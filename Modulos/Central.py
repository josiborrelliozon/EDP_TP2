from Contactos import *
from AppStore import *
from Mail import *
from datetime import datetime, timedelta
from Configuracion import *
#from CalculadoraGrafica import *
import numpy as np
from Telefono import *



#En el siguiente archivo, se encuentran las clases: Telefono, TelefonoApp, Central, MensajesApp y SMS (clase abstacta invocada en MensajesApp) y el MAIN


class MensajesApp(): #viene por Default en el telefono -> creo instancias de esta clase a través de un atributo en Telefono
    def __init__(self):
        self.sms_recibidos = []
        self.sms_enviados = []

    def enviar_sms(self, numero, mensaje):
        """
        Envía un mensaje SMS a un número registrado en la Central.

        Verifica que el número de destino esté registrado en la Central antes de enviar el SMS. Si el número no está registrado, lanza un error.
        Si el número está registrado, crea un objeto `SMS` y lo agrega a la lista de mensajes enviados.

        Parámetros:
        ----------
        numero : str
            Número de teléfono al cual se enviará el mensaje SMS.
        mensaje : str
            Contenido del mensaje SMS a enviar.
        """

        #envia un mensaje SMS introduciendo un numero de destinatario
        if not any(telefono.numero == numero for telefono in Central.telefonos_registrados.values()): #verifica que el numero este regstrado en la Central
            raise ValueError('Número no registrado')
        else:
            aux = SMS(numero, mensaje, datetime.now())
            self.sms_enviados.append(aux)
            print('Mensaje enviado:')
            print(f'    {aux}')

    def cargar_mensaje(self, numero, mensaje, fecha):
        """
        Carga un mensaje SMS recibido, agregándolo a la lista de mensajes recibidos.

        Crea un objeto `SMS` con el número de teléfono, mensaje y fecha proporcionados, y lo agrega a la lista de mensajes recibidos.

        Parámetros:
        ----------
        numero : str
            Número de teléfono del remitente del mensaje SMS.
        mensaje : str
            Contenido del mensaje SMS recibido.
        fecha : datetime
            Fecha y hora en que se recibió el mensaje SMS.
        """
        #Genera mensajes (simula que recibo mensajes)
        aux = SMS(numero, mensaje, fecha)
        self.sms_recibidos.append(aux)
        print(f'Mensaje recibido de {numero}')

    def visualizar_entrada(self):
        """
        Muestra todos los mensajes SMS recibidos, ordenados por fecha de envío, de más reciente a más antigua.

        Esta función ordena la lista de mensajes SMS recibidos según la fecha de envío, de modo que los mensajes más recientes aparecen primero, y luego imprime cada mensaje en la bandeja de entrada.

        Parámetros:
        ----------
        Ninguno

        Salida:
        -------
        Imprime en la consola los mensajes SMS recibidos en orden descendente por fecha de envío.
        """
        #Devuelve todos los SMS recibidos
        recibidos = sorted(self.sms_recibidos, key=lambda x: x.fecha_envio, reverse=True)
        print("Bandeja de entrada SMS:")
        for sms in recibidos:
            print(f'    {sms}')

    def eliminar_mensaje(self, numero, mensaje, fecha):
        """
        Elimina un mensaje SMS recibido de la bandeja de entrada.

        Esta función busca un mensaje en la lista de mensajes SMS recibidos que coincida con el número, el contenido del mensaje y la fecha de envío especificados. Si se encuentra el mensaje, se elimina de la lista. Si no se encuentra, se lanza una excepción.

        Parámetros:
        ----------
        numero : str
            El número del remitente del mensaje SMS a eliminar.
        mensaje : str
            El contenido del mensaje SMS a eliminar.
        fecha : datetime
            La fecha de envío del mensaje SMS a eliminar.

        Salida:
        -------
        Imprime un mensaje indicando que el mensaje ha sido eliminado o lanza una excepción si no se encuentra el mensaje.
        """
        # Elimina mensajes recibidos
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
        fecha_formateada = self.fecha_envio.strftime("%b%d %H:%M")
        return f'{self.numero} ({fecha_formateada}): {self.mensaje} '

class TelefonoApp():  #viene por Default en el telefono -> creo instancias de esta clase a través de un atributo en Telefono
    def __init__(self):
        self.llamadas = []

    def llamar(self, numero_propio, numero_entrante):
        """
        Realiza una llamada entre dos números. Primero verifica que ninguno de los dos números
        esté ocupado en una llamada, que el número entrante esté registrado y tenga conexión a
        la red, y luego agrega la llamada a la lista de llamadas en curso.

        Parámetros:
        -----------
        numero_propio : str
            El número desde el cual se realiza la llamada.
        numero_entrante : str
            El número al cual se realiza la llamada.

        Excepciones:
        ------------
        ValueError: Si el número está ocupado, no está registrado, o si la red no está disponible.
        """

        #crea una llamada entre los dos numeros introducidos
        for llamadas in Central.llamadas_en_curso:
            if numero_entrante in llamadas: #si el numero está en una llamada en curso
                raise ValueError("Numero ocupado")
            elif numero_propio in llamadas:
                raise ValueError("Para realizar nueva llamada debes cortar")

        if Central.verificar_numero(numero_entrante): #verifica que el numero se encuentre registrado
            if Central.verificar_red(numero_entrante):  #verifica conexión a red
                print("llamando ...")
                Central.llamadas_en_curso.append((numero_propio, numero_entrante))
            else:
                raise ValueError("Número fuera de servicio")

        else:
            raise ValueError("Numero no registrado")


    def atender(self, numero_propio, numero_saliente):
        """
        Atiende una llamada entrante. Primero verifica que el número propio no esté en
        una llamada en curso. Si es posible, agrega la llamada a la lista de llamadas en curso.

        Parámetros:
        -----------
        numero_propio : str
            El número que atiende la llamada.
        numero_saliente : str
            El número que está realizando la llamada entrante.

        Excepciones:
        ------------
        ValueError: Si el número propio ya está en una llamada en curso.
        """

        for llamadas in Central.llamadas_en_curso:
            if numero_propio in llamadas:
                raise ValueError("Para realizar nueva llamada debes cortar")
        Central.llamadas_en_curso.append((numero_propio, numero_saliente))

    def cortar(self, numero_propio, numero):
        """
        Corta una llamada en curso entre el número propio y el número dado. Verifica si existe una llamada activa
        entre los dos números, la elimina de la lista de llamadas en curso y registra la fecha de finalización.

        Parámetros:
        -----------
        numero_propio : str
            El número que está cortando la llamada.
        numero : str
            El número con el que se está realizando la llamada.

        Excepciones:
        ------------
        ValueError: Si no hay una llamada en curso entre los dos números.
        """

        # Crear una lista de los números, en cualquier orden
        lista_a_eliminar = {numero_propio, numero}  # Usamos un conjunto para ignorar el orden

        # Verificar si una llamada en curso contiene estos números
        llamada_existente = any(set(llamada) == lista_a_eliminar for llamada in Central.llamadas_en_curso)

        if llamada_existente:
            # Remover la llamada de Central.llamadas_en_curso
            Central.llamadas_en_curso = [llamada for llamada in Central.llamadas_en_curso if
                                         set(llamada) != lista_a_eliminar]

            fecha_formateada = datetime.now().strftime('%d-%m-%Y %H:%M') #Doy formato prolijo para la impresion

            # Registrar la llamada finalizada con la fecha de finalización
            self.llamadas.append((numero, fecha_formateada)) #En el App propia de llamadas
            Central.historico_llamadas.append((numero_propio, numero, f'fecha_realizacion: {fecha_formateada}')) #En el historico de llamadas de la Central
            print("Llamada finalizada.")
        else:
            raise ValueError("No hay llamada en curso.")



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

    def baja_id(self, telefono): # Se da de baja un id y se desregistra el telefono
       if telefono.id_central not in Central.telefonos_registrados.keys():
           raise ValueError("Este numero no se encuentra registrado")
       else:
           id_eliminado = Central.telefonos_registrados.pop(telefono.id_central)
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



try:
    if __name__=='__main__':
        #creo instancias de telefono:
        Central.crear_telefono("telefono_juanpi", "Nacho","Iphone", "X", "IOS", 20, 12345678, 12 )
        telefono_nacho = Telefono( "Nacho", "Iphone", "X", "IOS", 20, 500, 12345678, 400 )
        telefono_nacho.configuracion.configuracion_cambiar_nombre_telefono('Nachito')
        print(telefono_nacho)
        telefono_jose = Telefono( "Jose", "Iphone", "X", "IOS", 20, 600, 87654321, 400)
        telefono_agus = Telefono( "Agus", "Nokia", "nok", 8, 500, 100, 11112222, 21)
        telefono_fede = Telefono( "Telefono de Fede", "cubo", "nok", 8, 500, 123, 11113333, 21)
        telefono_pedro = Telefono( "Telefono de Pedro", "cubo", "nok", 8, 500, 123, 11110000, 21)
        telefono_nacho.on_off() #prendo el telefono
        telefono_nacho.desbloquear() #desbloqueo telefono
        telefono_nacho.conexion_internet() #conecto a internet
        telefono_nacho.conexion_red() #conecto a la red
        telefono_pedro.on_off()
        telefono_pedro.desbloquear()
        telefono_pedro.conexion_red()
        print(telefono_nacho)
        print(Central.numeros_existentes)

        print(".....................Pruebo conexion a red................................")

        telefono_jose.on_off() #prendo telefono
        telefono_jose.conexion_red() #conecto a la red
        print(Central.numeros_conectados_red)
        print(telefono_nacho.estado_red)

        print("..........................Pruebo Mail............................")

        #cargo los mails
        telefono_nacho.mail_app.cargar_mail(datetime(2024, 10, 10, 1), "agus@gmail.com", "nacho@gmail.com",
                              "Estamos muy complicados con el TP. Que hacemos?", "TP Estructuras", True)
        telefono_nacho.mail_app.cargar_mail(datetime(2024, 11, 7, 12), "jose@gmail.com", "nacho@gmail.com",
                              "Hay que pedirle ayuda a Fede. Abrazo.", "RE: TP Estructuras")
        telefono_nacho.mail_app.cargar_mail(datetime(2023, 11, 7, 12), "jose@gmail.com", "nacho@gmail.com",
                              "Adjunto a continuacion la tabla de datos", "Parcial de Quimica")
        telefono_nacho.mail_app.cargar_mail(datetime.now() - timedelta(days=1), "pedro@hotmail", "nacho@gmail.com",
                              "te invitamos al partido del sabado", "Partido Sabado")
        telefono_nacho.mail_app.cargar_mail(datetime.now() - timedelta(days=1), "luis@itba.edu.ar", "nacho@gmail.com",
                              "La presentacion es el jueves, tenemos que tener el pwp preparado. Te adjunto los avances.",
                              "TP Estructuras", True)

        #Muestra buzon con mails cargados, ordenados por llegada reciente y apareciendo primero los no leidos
        telefono_nacho.buzon_mails()



        print("..........................Pruebo Central............................")
        claro = Central("Claro")

        print(Central.numeros_existentes)
        claro.alta_id(telefono_fede)
        claro.alta_id(telefono_pedro)
        claro.alta_id(telefono_nacho)
        claro.alta_id(telefono_jose)
        claro.alta_id(telefono_agus)

        print(Central.telefonos_registrados)

        claro.baja_id(telefono_fede)
        print(Central.telefonos_registrados)


        print("..........................Pruebo Contactos............................")

        telefono_nacho.nuevo_contacto("Jose Borrelli", 123456789, "jb@itba.edu.ar", "Av Santa Fe 1200")
        telefono_nacho.nuevo_contacto("Jose Sarasqueta", 912201831, "js@itba.edu.ar", "Av Cabildo 1200")
        print(telefono_nacho.contactos)
        telefono_nacho.actualizar_contacto(912201831, "Jose Sarasqueta ITBA" )  #NO ME ACUALIZA EL NOMBRE
        print(telefono_nacho.contactos)

        print("..........................Pruebo AppStore............................")

        #telefono_nacho.calculadora_grafica = CalculadoraGrafica()
        #telefono_nacho.calculadora_grafica.factorial(5)
        #telefono_nacho.instalar_app("spotify") # tengo que vincular app store con spotify

        print("........................Pruebo Mensajes APP SMS............................")

        telefono_nacho.cargar_mensaje(11112222, 'Hoy no puedo :(' , datetime(2024,2,3,11))
        telefono_nacho.cargar_mensaje(34345656, 'No me sale estooo', datetime(2024,11,3,12))
        telefono_nacho.cargar_mensaje(34345656, 'Buenas tardes', datetime(2024, 10, 13, 12))
        telefono_nacho.visualizar_entrada()
        telefono_nacho.enviar_sms(11112222, "Hola como estas")
        telefono_nacho.eliminar_mensaje(11112222, 'Hoy no puedo :(' , datetime(2024,2,3,11))
        telefono_nacho.visualizar_entrada()

        print("..........................Pruebo Llamada............................")
        print(Central.telefonos_registrados)
        print(Central.verificar_numero(11110000))
        #telefono_fede.llamar(1213) #pruebo condicion: llamar sin estar conectado a red
        #telefono_nacho.llamar(12) #pruebo condicion: llamar a numero no existente
        #telefono_nacho.llamar(11110000) #pruebo condicion: llamar un numero fuera de servicio

        telefono_nacho.llamar(87654321)

        #telefono_nacho.llamar(921) #pruebo condicion: no puedo llamar a otro numero al estar en llamada
        #telefono_pedro.llamar(87654321) #pruebo condicion: llamo a un numero ocupado
        # telefono_nacho.atender(11110000) #pruebo condicion: no puedo atender a otro numero al estar en llamada

        telefono_agus.on_off()
        telefono_agus.desbloquear()
        telefono_agus.conexion_red()
        telefono_pedro.atender(11112222) #atiendo a un numero desocupado y conectado a red

        print(Central.llamadas_en_curso)

        telefono_nacho.cortar(87654321)
        print(Central.llamadas_en_curso)
        print(Central.historico_llamadas)



        print("..........................Pruebo Calculadora............................")
        #telefono_nacho.calculadora_grafica.calcular_polinomios('x**2 - 2*x + 1', 3000)
        #telefono_fede.calculadora_grafica.factorial(5)
        #telefono_agus.calculadora_grafica.normal(np.random.normal(loc=0, scale=1, size=1000))#genero data sets random
        #telefono_jose.calculadora_grafica.desvio([27,25,42,88,15,22,21,15,24,63,73,42,23,12,10,21,21,21,2,12,12,1,21,21,21])



except ValueError as e:
    print(e)



