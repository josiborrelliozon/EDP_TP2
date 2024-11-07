pip install numpy matplotlib sympy

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

class CalculadoraGrafica:
    def __init__(self):
        # Inicialización de la clase
        self.x = sp.symbols('x')  # Definir la variable simbólica

    def evaluar(self, expresion, valores):
        """
        Evalúa una expresión matemática para un conjunto de valores de x.
        :param expresion: Una cadena que representa una expresión matemática (por ejemplo, 'x**2 + 2*x + 1').
        :param valores: Un array de valores para evaluar la expresión.
        :return: Array con los resultados de la evaluación.
        """
        # Convertir la cadena en una expresión simbólica
        exp = sp.sympify(expresion)
        # Convertir la expresión simbólica en una función numérica
        f = sp.lambdify(self.x, exp, 'numpy')
        # Evaluar la expresión para los valores dados
        return f(valores)

    def graficar(self, expresion, x_range=(-10, 10), puntos=100):
        """
        Grafica la expresión matemática en un rango de valores de x.
        :param expresion: Una cadena con la expresión matemática a graficar (por ejemplo, 'x**2 + 2*x + 1').
        :param x_range: Un rango para los valores de x (por defecto, de -10 a 10).
        :param puntos: Número de puntos a generar para graficar.
        """
        # Crear un rango de valores para x
        x_vals = np.linspace(x_range[0], x_range[1], puntos)
        # Evaluar la expresión para los valores de x
        y_vals = self.evaluar(expresion, x_vals)
        # Graficar la función
        plt.plot(x_vals, y_vals, label=expresion)
        plt.title(f'Gráfico de {expresion}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()

    def calcular(self, expresion, valor_x):
        """
        Calcula el valor de una expresión para un valor dado de x.
        :param expresion: Una cadena con la expresión matemática a evaluar.
        :param valor_x: El valor específico de x para evaluar la expresión.
        :return: El resultado de la evaluación.
        """
        # Evaluar la expresión con el valor de x
        resultado = self.evaluar(expresion, np.array([valor_x]))
        return resultado[0]


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la calculadora gráfica
    calc = CalculadoraGrafica()

    # Definir la expresión
    expresion = 'x**2 + 2*x + 1'

    # Graficar la expresión
    calc.graficar(expresion, x_range=(-5, 5))

    # Calcular el valor de la expresión en x = 3
    resultado = calc.calcular(expresion, 3)
    print(f"El valor de la expresión en x = 3 es: {resultado}")
