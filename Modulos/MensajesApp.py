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