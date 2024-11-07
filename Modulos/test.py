class App:
    apps_existentes = []
    def __init__(self, id_app, espacio, nombre_app):
        self.id_app = id_app
        self.espacio = espacio
        self.nombre = nombre_app

        App.apps_existentes.append(self.id_app)

class mailApp(App):
   def __init__(self, espacio, id_app, nombre_app):
       super().__init__(espacio, id_app, nombre_app)
       self.bandeja = ["mail 1", "mail 2", "mail 3"]
   def visualizar_por_fecha(self):
       print("Bienvenido a GMAIL! :)")
       for i in range(len(self.recibidos)-1,-1,-1):
           print("%s\n",self.recibidos[i])




def main():
    my_app=mailApp("5","1","Gmail")
    mailApp.pantalla_de_inicio(my_app)

if __name__ == '__main__':
    main()