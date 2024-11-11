from Central import *

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