from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.solvers import solve
from sympy.parsing.sympy_parser import parse_expr

def solver_diff_app():

    x = symbols('x')

    init_printing(use_unicode=True)

    uno = str(input("\t\tIngresa la primera función"))
    dos = str(input("\t\tIngresa la segunda función"))

    ecuacion = parse_expr(uno)
    ecuacion2 = parse_expr(dos)

    velocidad = diff(ecuacion, x)
    velocidad2 = diff(ecuacion2, x)

    aceleracion = diff(velocidad, x)
    aceleracion2 = diff(velocidad2, x)

    # Ecuaciones parseadas
    parse_ecuacion = lambdify(x, ecuacion, 'numpy')
    parse_ecuacion2 = lambdify(x, ecuacion2, 'numpy')

    parse_velocidad = lambdify(x, velocidad, 'numpy')
    parse_velocidad2 = lambdify(x, velocidad2, 'numpy')

    parse_aceleracion = lambdify(x, aceleracion, 'numpy')
    parse_aceleracion2 = lambdify(x, aceleracion2, 'numpy')

    is_equal_v = solve(velocidad - velocidad2, x)
    is_equal_a = solve(aceleracion - aceleracion2, x)

    # Funciones que grafican

    # Grafica de la función
    def f(y):
        return parse_ecuacion(y)
    def g(y):
        return parse_ecuacion2(y)

    # Grafica de la velocidad
    def h(y):
        return parse_velocidad(y)
    def i(y):
        return parse_velocidad2(y)

    # Grafica de la aceleración
    def j(y):
        return parse_aceleracion(y)
    def k(y):
        return parse_aceleracion2(y)

    v=[-10,10,-8,5]   # para x de 0 a 10, para y de -5 a 5, se complementa con 
                    # el ultimo comando



    intervalo=np.linspace(0,10,50)
    plt.grid(True) #cuadriculas

    plt.ylabel('y') # eje y
    plt.xlabel('x') # eje x 
                    
    # primer plot

    plt.figure(1)

    plt.ylim(-10, 10)
    plt.title('Representación gráfica')
    plt.plot(intervalo,f(intervalo),'r-',label='Primera figura')
    plt.plot(intervalo,g(intervalo),'r-',label='Segundo figura', color="blue")

    # segundo plot
    plt.subplot(222)
    # plt.title('Tienen la misma velocidad')
    plt.annotate('velocidades', xy=(is_equal_v[0], parse_aceleracion(is_equal_v[0])), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
    )
    plt.xlim(-1, 6)
    plt.ylim(-3, 3)
    plt.plot(intervalo, h(intervalo), 'r-',label='velocidad', color="blue")
    plt.plot(intervalo, i(intervalo), 'r-',label='velocidad', color="red")

    # tercer plot
    plt.subplot(223)
    # plt.title('Tienen la misma rapidez')
    plt.xlim(-1, 6)
    plt.ylim(-7, 3)
    print(is_equal_a)
    print(f'\t\t\tLa aceleración es igual en: x = {is_equal_a[0]} y = {parse_aceleracion(is_equal_a[0])}')

    plt.legend(loc=1)
    plt.axis(v)

    plt.show()