from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np  # Permite manejar datos, añade funciones trigonometricas

x = Symbol('x') # Define una variable en la ecuación sympy

ecuacion = str(input('ecuación')) # La ecuación
ecuacionParseada = parse_expr(ecuacion) # La ecuación parseada
derivada = diff(ecuacionParseada, x) # La derivada

# lambdify te permite permite adapatar la ecuación para sustituir la variable x por número
derivadaNumpy = lambdify(x, derivada, 'numpy') # la derivada adaptada a numpy
ecuacionNumpy = lambdify(x, ecuacionParseada, 'numpy') # la ecuación adaptada a numpy

# que hace lambdify
# Si la ecuación es x² lambdify te permite cambiar la X por un número
# parse_expr convierte el string a una ecuación
