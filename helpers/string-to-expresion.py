from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x = Symbol('x') # Define una variable en la ecuación sympy

def string_to_expresion(string):
    global x

    ecuacionParseada = parse_expr(string) # La ecuación parseada

    return ecuacionParseada

    # que hace lambdify
    # Si la ecuación es x² lambdify te permite cambiar la X por un número
    # parse_expr convierte el string a una ecuación
