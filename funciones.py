from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np 
import matplotlib.pyplot as plt

y = symbols('x')

x=np.linspace(-10,10,100)
ecuacion = str(input('ecuación ')) # La ecuación
ecuacionParseada = parse_expr(ecuacion) # La ecuación parseada
ecuacionNumpy = lambdify(y, ecuacionParseada, 'numpy')

plt.plot(x, ecuacionNumpy(x), 'r')
plt.title(f'la función {ecuacion}')
plt.grid()