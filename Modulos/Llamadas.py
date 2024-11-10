from Central import *

from datetime import datetime, timedelta

class TelefonoApp():  #viene por Default en el telefono -> creo instancias de esta clase a través de un atributo en Telefono
    def __init__(self):
        self.llamadas = []

    def llamar(self, numero_propio, numero_entrante):
        for tupla_llamadas in Central.llamadas_en_curso:
            if (numero_entrante in tupla_llamadas) or (numero_propio in tupla_llamadas): #si el numero está en una llamada en curso
                raise ValueError("Numero ocupado")
        if numero_entrante not in Central.telefonos_registrados.values():
            raise ValueError("Numero invalido")
        else:
            print("llamando ...")
            Central.llamadas_en_curso.append(list(zip(numero_propio, numero_entrante)))

    def atender(self, numero_propio, numero_saliente):
        Central.llamadas_en_curso.append((numero_propio, numero_saliente))

    def cortar(self, numero_propio, numero):
        lista_a_eliminar = [numero_propio, numero] # lista a eliminar
        if lista_a_eliminar in Central.llamadas_en_curso: # Eliminar la tupla
            Central.llamadas_en_curso.remove(lista_a_eliminar)

        self.llamadas.append((numero,f'fecha_realizacion: {datetime.now()}'))





try:
    if __name__=='__main__':
        telefono_josi = TelefonoApp()
        #telefono_josi.llamar(12345678, 87654321) #chequeo condicion de numero ocupado
        print(Central.telefonos_registrados.values())
        telefono_josi.llamar(11111111, 69696969)
        print(Central.llamadas_en_curso)

except ValueError as e:
    print(e)











