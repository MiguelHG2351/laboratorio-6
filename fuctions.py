import os
from time import sleep
from sympy import lambdify, symbols
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import numpy as np


class Solver_functions():

    def __init__(self):
        self.x = symbols('x')

    def graph(self):

        limit_left = -10
        limit_right = 10

        os.system('cls')
        print("Ingrese la función a graficar\n")
        equation = str(input('ƒ(x) = '))
        parse_equation = ''

        try:
            equation = int(equation)
        except:
            parse_equation = lambdify(self.x,parse_expr(equation),'numpy')

        def graph(x):
            #Si equation se cambio a entero, retorna esto
            if(type(equation) is int) == True:
                print("Es entero")
                return np.full(x.shape,equation)
            else:
                return parse_equation(x)
        xRange = np.linspace(limit_left,limit_right)

        plt.grid(True)
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.plot(xRange,graph(xRange),'g')
        plt.axis('auto')
        plt.title(f'ƒ(x) = {(equation)}')
        plt.ylabel('ƒ (x)')
        plt.show()


    def solver_functions(self):
        os.system('cls')

        print('\u001b[33;1m\t\t\t\t\t\t\tGraficas de una Función | Matemáticas I')

        try:
            self.graph()
            sleep(2)
        except ValueError:
            print('\u001b[31;1m\t\t>>> Error de opciones')
            # Regresa los colores a la normalidad
            print("\033[0;37;48m \033[0;37;48m")
            sleep(1)
