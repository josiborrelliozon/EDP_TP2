from Central import *

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



