from sympy import *
from sympy.parsing.sympy_parser import parse_expr #Convierte string a ecuacion
import numpy as np
import matplotlib.pyplot as plt
import sys, time, os

x = Symbol('x')

def menu():
    os.system('cls')
    global x

    print("= = = = Laboratorio #6 = = = =\n\n")
    print("=> [1] Graficar una función\n\n=> [2] Calcular el límite de una función\n\n=> [3] Salir\n\n")

    Select = int(input("Seleccione una opción [ ]\b\b"))

    if Select == 1:
        os.system('cls')
        while True:
            graph_function()
            answer = str(input('Desea ingresar otra función ?'))

            if(answer.lower() != 'si'):
                 menu()

    elif Select == 2:
        os.system('cls')
        print("Ingrese la función para calcular el límite")
    elif Select == 3:
        print("Adiós!")
        exit()
    else:
        os.system('cls')
        print("Seleccione una opcion valida")
        time.sleep(3)
        menu()

def graph_function():

    global x
    limit_left = -10
    limit_right = 10

    try:
        os.system('cls')
        print("Ingrese la función a graficar\n")
        equation = str(input('ƒ(x) = '))
        ParseEquation = parse_expr(equation)
        Numpyequation = lambdify(x,ParseEquation,'numpy')

        def graph(x):
            return Numpyequation(x)

        xRange = np.linspace(limit_left,limit_right)

        plt.grid(True)
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.plot(xRange,graph(xRange),'g')
        plt.axis('auto')
        plt.title(f'ƒ(x) = {(equation)}')
        plt.ylabel('ƒ (x)')
        plt.show()
    except:
        print("\nEcuación incorrecta!")

menu()