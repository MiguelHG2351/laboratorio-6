from sympy import *
import numpy as np
import os,time

x = Symbol('x')

def limits():
    global x
    os.system('cls')
    print("= = => Ingrese la función para calcular el límite <= = =\n")
    equation = str(input('ƒ(x) = '))
    parseEquation = parse_expr(equation)
    xValue = str(input("\nIngrese el valor de x : "))
    parse_xValue = parse_expr(xValue)

    lim = limit(parseEquation,x,parse_xValue)

    print("\n=> El límite es: {}".format(lim))

def limit_lat():
    global x
    os.system('cls')
    print("= = => Ingrese la función para calcular el límite <= = =\n")
    equation = str(input('ƒ(x) = '))
    parseEquation = parse_expr(equation)
    xValue = str(input("\nIngrese el valor de x : "))
    parse_xValue = parse_expr(xValue)
    sideValue = str(input("\nEl límite tiende por la derecha o izquierda ?"))
    """parse_sideValue = parse_expr(sideValue)"""

    if sideValue == '+' or sideValue == '-':
        lim = limit(parseEquation,x,parse_xValue,sideValue)
        print("\n=> El límite es: {}".format(lim))

def limits_menu():
    os.system('cls')
    print("[1] => Calcular el límite de una función\n\n[2] => Calcular el límite de una función lateral\n\n[3] => Atrás\n\n")
    option = int(input("Opción [ ]\b\b"))

    if option == 1:
        while True:
            limits()
            answer = str(input('\nDesea ingresar otra función ?'))
            if(answer.lower() != 'si'):
                limits_menu()
    elif option == 2:
        while True:
            limit_lat()
            answer = str(input('\nDesea ingresar otra función ?'))
            if(answer.lower() != 'si'):
                limits_menu()
    elif option == 3:
        exit()
    else:
        os.system('cls')
        print("Seleccione una opción valida")
        time.sleep(3)
        limits_menu()

limits_menu()