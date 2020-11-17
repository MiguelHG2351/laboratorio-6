from sympy import *
import os
import numpy as np  # Permite manejar datos, añade funciones trigonometricas
import matplotlib.pyplot as plt  # Permite graficar
from sympy.parsing.sympy_parser import parse_expr #Convierte string a ecuacion



x = Symbol('x')

os.system('cls')
print("Ingrese la función a graficar\n")
equation = str(input('ƒ(x) = '))
equationParse = ''

# Intenta convertir a entero
try:
    equation = int(equation)

# No puedes :'v, intenta hacerlo ecuación
except:
    equationParse = lambdify(x,parse_expr(equation),'numpy')

def graph(x):
    # Si equation se cambio a entero, retorna esto
    if (type(equation) is int) == True:
        return np.full(x.shape, equation)
    else:
        return equationParse(x)

xRange = np.linspace(-2,2)

plt.grid(True)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.plot(xRange, graph(xRange),'g')
plt.axis('auto')
plt.title(f'ƒ(x) = {(equation)}')
plt.ylabel('ƒ (x)')
plt.savefig('foo.png')
plt.show()