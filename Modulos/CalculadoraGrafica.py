import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import seaborn as sns
from scipy.stats import norm

class CalculadoraGrafica:
    def __init__(self):
        self.x = sp.symbols('x')

    def factorial(self, n): #metodo en el q se imprime el factorial
        print(f'El factorial de {n} es {self.factorial_auxiliar(n)}')

    def factorial_auxiliar(self, n): # funcion recursiva para realizar el factorial
        if n == 0:
            return 1
        else:
            return n * self.factorial_auxiliar(n - 1)

    def evaluar(self, expresion, valores):
        exp = sp.sympify(expresion)
        f = sp.lambdify(self.x, exp, 'numpy')
        return f(valores)

    def graficar(self, expresion, x_range=(-10, 10), puntos=100):

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
        resultado = self.evaluar(expresion, np.array(valor_x))
        print(f'El resultado de {expresion} al evaluar en {valor_x} es {resultado}')

    def calcular(self, expresion):
        resultado = self.evaluar(expresion,1)
        print(f'El resultado es {float(resultado)}')
    def normal(self, data):
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
        print(f'El desvio estandar del data set es {np.std(data)}')


if __name__ == "__main__":
    calc = CalculadoraGrafica()
    data = np.random.normal(loc=0, scale=1, size=1000)
    expresion = 'x**4 + x**2 - 2*x + 1'
    calc.calcular_polinomios(expresion, [1, 2])
    calc.graficar(expresion, x_range=(-5, 5))
    calc.factorial(10)
    calc.calcular(4/5)
    calc.normal(data)
