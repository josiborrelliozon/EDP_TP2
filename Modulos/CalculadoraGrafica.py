import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import seaborn as sns
from scipy.stats import norm

class CalculadoraGrafica:
    def __init__(self):
        self.x = sp.symbols('x')

    def factorial(self, n):
        """
            Calcula e imprime el factorial de un número.

            Utiliza el método auxiliar para calcular el factorial y luego imprime el resultado.

            Parámetros:
                n (int): El número del cual se calculará el factorial."""

        print(f'El factorial de {n} es {self.factorial_auxiliar(n)}')

    def factorial_auxiliar(self, n):
        """
            Calcula el factorial de un número de manera recursiva.

            Este método recursivo devuelve el factorial de un número entero `n`, donde
            el factorial de 0 es definido como 1.

            Parámetros:
                n (int): El número del cual se calculará el factorial.

            Retorna:
                int: El factorial de `n`. """
        if n == 0:
            return 1
        else:
            return n * self.factorial_auxiliar(n - 1)

    def evaluar(self, expresion, valores):
        """
            Evalúa una expresión simbólica en una lista de valores.

            Parámetros:
            expresion : str - Expresión simbólica.
            valores : array-like - Valores para evaluar la expresión.

            Retorna:
            Resultado de la evaluación para cada valor en 'valores'.
            """
        exp = sp.sympify(expresion)
        f = sp.lambdify(self.x, exp, 'numpy')
        return f(valores)

    def graficar(self, expresion, x_range=(-10, 10), puntos=100):
        """
           Grafica una expresión simbólica en un rango específico de valores de x.

           Parámetros:
           ----------
           expresion : str
               La expresión matemática a graficar, en formato de cadena.
           x_range : tuple, opcional
               El rango de valores de x para graficar (por defecto es (-10, 10)).
           puntos : int, opcional
               La cantidad de puntos a evaluar dentro del rango (por defecto es 100).

           -------
               Muestra el gráfico de la expresión en el rango de valores de x especificado.
           """
        x_vals = np.linspace(x_range[0], x_range[1], puntos)
        y_vals = self.evaluar(expresion, x_vals)
        plt.plot(x_vals, y_vals, label=expresion)
        plt.title(f'Gráfico de {expresion}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()

    def calcular_polinomios(self, expresion, valor_x):
        """
            Grafica una expresión simbólica en un rango específico de valores de x.

            Parámetros:
            ----------
            expresion : str
                La expresión matemática a graficar, en formato de cadena.
            x_range : tuple, opcional
                El rango de valores de x para graficar (por defecto es (-10, 10)).
            puntos : int, opcional
                La cantidad de puntos a evaluar dentro del rango (por defecto es 100).
            """
        resultado = self.evaluar(expresion, np.array(valor_x))
        print(f'El resultado de {expresion} al evaluar en {valor_x} es {resultado}')

    def calcular(self, expresion):
        """
        Calcula el valor de una expresión simbólica al evaluarla en x = 1.

        Parámetros:
        ----------
        expresion : str
            La expresión matemática a evaluar, en formato de cadena.
        """

        resultado = self.evaluar(expresion,1)
        print(f'El resultado es {float(resultado)}')

    def normal(self, data):
        """
        Ajusta y grafica la distribución normal a un conjunto de datos.

        Parámetros:
        ----------
        data : array-like
            Conjunto de datos numéricos sobre los cuales se ajustará la distribución normal.
        """

        mean = np.mean(data)
        std_dev = np.std(data)
        plt.figure(figsize=(10, 6))
        sns.histplot(data, bins=30, kde=True, color='blue', stat='density', linewidth=0, label='Datos')
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, std_dev)
        plt.plot(x, p, 'k', linewidth=2, label='Distribución Normal Ajustada')
        plt.title('Distribución Normal Ajustada a los Datos')
        plt.xlabel('Valor')
        plt.ylabel('Densidad')
        plt.legend()
        plt.show()

    def desvio(self,data):
        """
        Calcula y muestra el desvío estándar de un conjunto de datos.

        Parámetros:
        ----------
        data : array-like
            Conjunto de datos numéricos sobre el que se calculará el desvío estándar.
        """

        print(f'El desvio estandar del data set es {np.std(data)}')


if __name__ == "__main__":

    #pruebo si me funciona el docstring
    print(CalculadoraGrafica.desvio.__doc__)

    #___
    calc = CalculadoraGrafica()
    data = np.random.normal(loc=0, scale=1, size=1000)
    expresion = 'x**4 + x**2 - 2*x + 1'
    calc.calcular_polinomios(expresion, [1, 2])
    calc.graficar(expresion, x_range=(-5, 5))
    calc.factorial(10)
    calc.calcular(4/5)
    calc.normal(data)
