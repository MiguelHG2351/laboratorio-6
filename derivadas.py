import os
from time import sleep
from sympy import diff, symbols
from sympy.parsing.sympy_parser import parse_expr


class Solver_diff():

    def __init__(self):
        self.x = symbols('x')

    def derivar(self, ec):

        try:
            return diff(parse_expr(ec), self.x)

        except:
            print('\u001b[31;1m\t\t>>> Ingreso una Derivada incorrecta')

    def solver_diff(self):
        os.system('cls')

        print('\u001b[33;1m\t\t\t\t\t\t\tDerivadas de una Función | Matemáticas I')

        ec = ''

        try:
            ec = str(input('\033[1;30;40m\t\tIngrese la función a derivar: f(x) = '))

            derivar_return = self.derivar(ec)
            print(f"La derivada es: f'() = {derivar_return}")
            sleep(2)
        except ValueError:
            print('\u001b[31;1m\t\t>>> Error de opciones')
            # Regresa los colores a la normalidad
            print("\033[0;37;48m \033[0;37;48m")
            sleep(1)
