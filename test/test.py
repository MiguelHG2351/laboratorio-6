
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np  # Permite manejar datos, añade funciones trigonometricas
import matplotlib.pyplot as pyplot  # Permite graficar

x = Symbol('x')

limit_left = -2 # Estos son los límites por defecto
limit_right = 2 # Estos son los límites por defecto

try:
    ecuacion = str(input('ecuación')) # La ecuación
    ecuacionParseada = parse_expr(ecuacion) # La ecuación parseada
    derivada = diff(ecuacionParseada, x) # La derivada
    derivadaNumpy = lambdify(x, derivada, 'numpy') # la derivada adaptada a numpy
    ecuacionNumpy = lambdify(x, ecuacionParseada, 'numpy') # la ecuación adaptada a numpy

    print('La derivada es:', derivada) # Imprime la derivada

    def graph(x):
        return ecuacionNumpy(x)

    # Si la derivada en ambos lados tiene los mismos valores en el eje y, ejecuta
    # abs es para no indicarle su monotonia

    state_change = 0
    
    while abs(ecuacionNumpy(limit_left)) / abs(ecuacionNumpy(limit_right)) >= 1.2 or abs(ecuacionNumpy(limit_right)) / abs(ecuacionNumpy(limit_left)) >= 1.2:
        
        if ecuacionNumpy(limit_left) > ecuacionNumpy(limit_right):
            limit_right += 1
            state_change += 1 
        elif ecuacionNumpy(limit_left) < ecuacionNumpy(limit_right):
            limit_left -= 1
            state_change -= 1

        # el contador aumenta dependiendo de donde se requiera adaptar la ecuación
        # Si se requiere adaptar la izquierda, el contador disminuye
        # cuando llega a adaptarse en el eje y, el valor cambia por lo que no es igual al valor de las iteraciones totales
        # por lo que cambio y ya debe terminar el ciclo
        if(abs(state_change) != limit_right - 2):
            break;

        # Pero si los valores crecen exponencialmente se disminuye la gráfica
        # Si en uno de sus lados es mayor que el otro, uno disminuye


    x = np.linspace(limit_left, limit_right)

    pyplot.plot(x, graph(x))
    pyplot.title(f'ƒ(x) = {ecuacion}')
    pyplot.show()
except:
    print('Ecuación incorrecta')