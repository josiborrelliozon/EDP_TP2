class App():
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio

    def __str__(self):
        return f'{self.nombre}, espacio = {self.espacio} Gb'

    def __repr__(self):
        return f'{self.nombre}, espacio = {self.espacio} Gb'