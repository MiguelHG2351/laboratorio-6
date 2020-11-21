import os
from time import sleep


class Solver_matrix():

    def matrix(self, cols, rows):

        matrix = []
        row = []

        for i in range(cols):
            row = []
            for j in range(rows):
                print(f'\t\tIngresa los valores de la columna {i} fila {j}')
                values = input(f'\t\t[{i}][{i}] = ')
                row.append(values)
            matrix.append(row)

        def rotar(matriz):
            rotada = []
            for i in range(len(matriz[0])):
                rotada.append([])
                for j in range(len(matriz)):
                    rotada[i].append(matriz[len(matriz)-1-j][i])
            return rotada

        return rotar(matrix)

    def solver_matrix(self):
        os.system('cls')

        print(
            '\u001b[33;1m\t\t\t\t\t\t\tMatrices de rotación, traslación y escalar | Matemáticas I')
        print(
            '\n\n\u001b[36m\t\t\t\tMatriz de Rotación\t\tMatriz de escalar\t\tMatriz de traslación')

        try:
            cols = int(
                input('\033[1;30;40m\t\tCuantas columnas tiene su matriz?'))
            rows = int(
                input('\033[1;30;40ma\t\tY en filas?'))

            matriz_return = self.matrix(cols, rows)
            print(f'El límite es: ')

            
            prettier_print = ''

            for i in range(len(matriz_return)):
                for j in range(len(matriz_return[i])):
                    prettier_print += '\t-\t' + matriz_return[i][j]
                prettier_print += '\n'

            print(f'\u001b[34;1m{prettier_print}')


            sleep(2)

        except ValueError:
            print('\u001b[31;1m\t\t>>> Error de opciones dentro de la matriz')

            # Regresa los colores a la normalidad
            print("\033[0;37;48m \033[0;37;48m")
            sleep(1)

# matrix=[]
# row=[]
# print('De cuantas columnas es su matriz')
# colInput = int(input())
# rowInput = int(input())
# values = 0

# for i in range(colInput): #total row is 3
#     row=[] #Credits for Hassan Tariq for noticing it missing
#     for j in range(rowInput): #total column is 3
#         print(f'\t\tIngresa los valores de la columna {i} fila {j}')
#         values = input(f'\t\t[{i}][{i}] = ')
#         row.append(values) #adding 0 value for each column for this row
#     matrix.append(row) #add fully defined column into the row


# def rotar(matriz):
#     rotada = []
#     for i in range(len(matriz[0])):
#         rotada.append([])
#         for j in range(len(matriz)):
#             rotada[i].append(matriz[len(matriz)-1-j][i])
#     return rotada


# for fila in matrix:
#     for e in fila:
#         print(e, end=" ")
#         print()

# print("-----------------------------")

# rotada = rotar(matrix)

# prettier_print = ''

# for i in range(len(rotada)):
#     for j in range(len(rotada[i])):
#         prettier_print += '\t-\t' + rotada[i][j]
#     prettier_print += '\n'

# print(prettier_print)
