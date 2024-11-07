from Central import *
import locale

locale.setlocale(locale.LC_TIME, 'es_ES')  #me pone las fechas relativas a Espana
from datetime import datetime, timedelta

class Llamada:
    def __init__(self, fecha_hora_inicio, fecha_hora_fin, entrante_saliente, realizada: bool):
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin
        self.entrante_saliente = entrante_saliente
        self.realizada = realizada
        self.duracion = fecha_hora_fin - fecha_hora_inicio

    def __str__(self):
        return f'{self.duracion}; {self.fecha_hora_inicio}; {self.entrante_saliente}; {self.realizada}'


class TelefonoApp():
    def __init__(self):
        self.llamadas = []

    def llamar(self, numero_propio, numero_entrante): #hacer wrapper
        for tupla_llamadas in Central.llamadas_en_curso:
            if (numero_entrante in tupla_llamadas) or (numero_propio in tupla_llamadas): #si el numero está en una llamada en curso
                raise ValueError("Numero ocupado")
            else:
                print("llamando ...")
                
                Central.llamadas_en_curso.append((numero_propio, numero_entrante))


    def atender(self, numero_propio, numero_saliente):
        Central.llamadas_en_curso.append((numero_propio, numero_saliente))

    def cortar(self, numero_propio, numero):
        tupla_a_eliminar = (numero_propio, numero) # Tupla a eliminar

        if tupla_a_eliminar in Central.llamadas_en_curso: # Eliminar la tupla
            Central.llamadas_en_curso.remove(tupla_a_eliminar)




try:
    if __name__=='__main__':
        telefono_josi = TelefonoApp()
        telefono_josi.llamar(12345678, 87654321)
        print(Central.llamadas_en_curso)

except ValueError as e:
    print(e)











