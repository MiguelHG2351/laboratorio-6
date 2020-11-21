import os
from time import sleep
from sympy import limit, symbols
from sympy.parsing.sympy_parser import parse_expr


class SolverMatrix():

    def __init__(self):
        self.x = symbols('x')

    def limit(self, ec, matriz):

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
            cols = str(input('\033[1;30;40m\t\tCuantas columnas tiene su matriz?'))
            rows = str(
                input('\033[1;30;40ma\t\tY en filas?'))
            direction = str(input('\033[1;30;40ma\t\tFinal aaaaaaaaaa'))

            limit_return = self.limit(ec, trending, direction)
            print(f'El límite es: {limit_return}')
            sleep(2)
        except ValueError:
            print('\u001b[31;1m\t\t>>> Error de opciones dentro de la matriz')
            # Regresa los colores a la normalidad
            print("\033[0;37;48m \033[0;37;48m")
            sleep(1)

matrix=[]
row=[]
print('De cuantas columnas es su matriz')
colInput = int(input())
rowInput = int(input())
values = 0

for i in range(colInput): #total row is 3
    row=[] #Credits for Hassan Tariq for noticing it missing
    for j in range(rowInput): #total column is 3
        print(f'Ingresa los valores de la columna {i} fila {j}')
        values = input('Ingrese la matriz')
        row.append(values) #adding 0 value for each column for this row
    matrix.append(row) #add fully defined column into the row


def rotar(matriz):
    rotada = []
    for i in range(len(matriz[0])):
        rotada.append([])
        for j in range(len(matriz)):
            rotada[i].append(matriz[len(matriz)-1-j][i])
    return rotada

for fila in matrix:
    for e in fila:
        print(e, end=" ")
        print()
        
print("-----------------------------")
    
rotada= rotar(matrix)
prettier_print = ''

for i in range(len(rotada)):
    for j in range(len(rotada[i])):
        prettier_print += '-' + rotada[i][j]
    prettier_print += '\n'

print(prettier_print)
