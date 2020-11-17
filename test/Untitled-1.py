
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np  # Permite manejar datos, añade funciones trigonometricas
import matplotlib.pyplot as pyplot  # Permite graficar

x = Symbol('x')

ecuacion = str(input('ecuación')) # La ecuación
ecuacionParseada = parse_expr(ecuacion) # La ecuación parseada
derivada = diff(ecuacionParseada, x) # La derivada
derivadaNumpy = lambdify(x, derivada, 'numpy') # la derivada adaptada a numpy
ecuacionNumpy = lambdify(x, ecuacionParseada, 'numpy') # la ecuación adaptada a numpy
x1 = int(input('ingrese el valor en el eje x')) # en que valor de X va
# y1 = input('ingrese el valor en el eje y')

print('La derivada es:', derivada) # Imprime la derivada

def graph(x):
    return ecuacionNumpy(x)


def tang(x):
    return derivadaNumpy(x1) * (x - x1) + ecuacionNumpy(x1) # Formula de la tangente


x = np.linspace(-2,2)

pyplot.plot(x, graph(x))
pyplot.plot(x, tang(x))
pyplot.title('Función f(x) = sen(x) + cos(2x)')
pyplot.show()