import os
from time import sleep
from sympy import limit, symbols
from sympy.parsing.sympy_parser import parse_expr


class SolverLimit():

    def __init__(self):
        self.x = symbols('x')

    def limit(self, ec, trending, direction=''):

        # simplify_expr = symplify(ec) -> Se obtuvo un problema cuando se intantaba factorizar

        if len(direction) == 1 and (direction.find('+') or direction.find('-')):
            return limit(parse_expr(ec), self.x, parse_expr(trending), direction)

        elif len(direction) == 0:
            return limit(parse_expr(ec), self.x, trending)

        else:
            print('\u001b[31;1m\t\t>>> Ingreso un Límite Incorrecto')

    def solver_limits(self):
        os.system('cls')

        print('\u001b[33;1m\t\t\t\t\t\t\tGráfica y Límite de una función | Matemáticas I')
        print('\n\n\u001b[36m\t\t\t\tLímite\t\tLimite Lateral')

        trending = ''
        ec = ''
        direction = ''

        try:
            ec = str(input('\033[1;30;40m\n\t\tIngrese el Límite de la función\t: ƒ(x)=  \u001b[32m'))
            trending = str(
                input('\033[1;30;40ma\n\t\tAhora tiene que darle una tendencia en el eje X: \u001b[32mx -> '))
            direction = str(input(f'\033[1;30;40m\n\n\t\tDirección del Límite: "+" o "-" si no presione enter: \u001b[32mx -> {trending} '))

            limit_return = self.limit(ec, trending, direction)
            print(f'El límite es: {limit_return}')
            sleep(2)
        except ValueError:
            print('\u001b[31;1m\t\t>>> Error de opciones')
            # Regresa los colores a la normalidad
            print("\033[0;37;48m \033[0;37;48m")
            sleep(1)
