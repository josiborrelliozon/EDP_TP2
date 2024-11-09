from Central import *

from datetime import datetime, timedelta

class TelefonoApp():
    def __init__(self):
        self.llamadas = []

    def llamar(self, numero_propio, numero_entrante):
        for tupla_llamadas in Central.llamadas_en_curso:
            if (numero_entrante in tupla_llamadas) or (numero_propio in tupla_llamadas): #si el numero está en una llamada en curso
                raise ValueError("Numero ocupado")
        if numero_entrante not in Central.telefonos_registrados:
            raise ValueError("Numero invalido")
        else:
            print("llamando ...")
            Central.llamadas_en_curso.append((numero_propio, numero_entrante))

    def atender(self, numero_propio, numero_saliente):
        Central.llamadas_en_curso.append((numero_propio, numero_saliente))

    def cortar(self, numero_propio, numero):
        tupla_a_eliminar = (numero_propio, numero) # Tupla a eliminar
        if tupla_a_eliminar in Central.llamadas_en_curso: # Eliminar la tupla
            Central.llamadas_en_curso.remove(tupla_a_eliminar)

        self.llamadas.append((numero,f'fecha_realizacion: {datetime.now()}'))





try:
    if __name__=='__main__':
        telefono_josi = TelefonoApp()
        telefono_josi.llamar(12345678, 87654321)
        print(Central.llamadas_en_curso)

except ValueError as e:
    print(e)











