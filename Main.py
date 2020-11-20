import os
from time import sleep
from limites import SolverLimit
from derivadas import Solverdiff
# from sympy.printing import printer


class Main(SolverLimit, Solverdiff):

    def select_option(self, select):
        os.system('cls')
        f = open('./logo.txt', "r")
        ascii = "".join(f.readlines())
        print(f'\t\t\t{ascii}')

        sleep(1)
        if select == 1:
            self.run()
        if select == 2:
            self.init()
        if select == 3:
            self.solver_limits()
        if select == 4:
            self.solver_diff()
        if select == 5:
            self.run()
        else:
            self.run()

    def run(self,):

        os.system('cls')

        # Regresa los colores a la normalidad
        print("\033[0;37;48m \033[0;37;48m")

        print('\u001b[33;1m\t\t\t\t\t\t\tProyecto Final de Matemáticas I')
        print(
            '\n\n\u001b[36m\t\tMatrices\t\tFunciones\t\tLímites\t\tDerivadas\t\tAplicaciones de la derivada')
        print(
            "\n\n\033[0;37;48m\t       (row, col)\t\t  f(x)\t\t\tLim f(x)\t  f'(x)\t\t\t\tf'(x)=🏠\033[0;37;48m")

        # Regresa los colores a la normalidad
        print("\033[0;37;48m \033[0;37;48m")

        select = 0
        try:
            select = int(
                input('\033[1;30;40m\n\t\tSelecciona que quieres hacer: \u001b[32m'))
            self.select_option(select)
        except ValueError:
            print(
                '\u001b[31;1m\t\t>>> Error de opciones, se ingreso un tipo de dato diferente al requerido')
            # Regresa los colores a la normalidad
            print("\033[0;37;48m \033[0;37;48m")
            sleep(1)
            self.run()


Main().run()
