
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np  # Permite manejar datos, añade funciones trigonometricas
import matplotlib.pyplot as pyplot  # Permite graficar

x = Symbol('x')

limit_left = -2 # Estos son los límites por defecto
limit_right = 2 # Estos son los límites por defecto

ecuacion = str(input('ecuación')) # La ecuación
ecuacionParseada = parse_expr(ecuacion) # La ecuación parseada
derivada = diff(ecuacionParseada, x) # La derivada
derivadaNumpy = lambdify(x, derivada, 'numpy') # la derivada adaptada a numpy
ecuacionNumpy = lambdify(x, ecuacionParseada, 'numpy') # la ecuación adaptada a numpy

print('La derivada es:', derivada) # Imprime la derivada

def graph(x):
    return ecuacionNumpy(x)

# Si la derivada en ambos lados tiene los mismos valores, ejecuta
# abs es para no indicarle su monotonia
while abs(ecuacionNumpy(limit_left)) / abs(ecuacionNumpy(limit_right)) >= 1.2 or abs(ecuacionNumpy(limit_right)) / abs(ecuacionNumpy(limit_left)) >= 1.2:
    if ecuacionNumpy(limit_left) > ecuacionNumpy(limit_right):
        limit_right += 1
    elif ecuacionNumpy(limit_left) < ecuacionNumpy(limit_right):
        limit_left += 1


# Pero si los valores crecen exponencialmente se disminuye la gráfica
# Si en uno de sus lados es mayor que el otro, uno disminuye


x = np.linspace(limit_left, limit_right)

pyplot.plot(x, graph(x))
pyplot.title(f'ƒ(x) = {ecuacion}')
pyplot.show()