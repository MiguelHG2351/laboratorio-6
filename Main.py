import os
from time import sleep
from limites import Solver_limit
from derivadas import Solver_diff
from matrix import Solver_matrix
from fuctions import Solver_functions
from diff_app import solver_diff_app
# from sympy.printing import printer


class Main(Solver_limit, Solver_diff, Solver_matrix, Solver_functions):

    def select_option(self, select):

        sleep(1)
        if select == 1:
            self.solver_matrix()
        if select == 2:
            self.solver_functions()
        if select == 3:
            self.solver_limits()
        if select == 4:
            self.solver_diff()
        if select == 5:
            solver_diff_app()
        if select == 6:
            print("\033[0;37;48m \033[0;37;48m")
            exit();
        else:
            self.run()

    def run(self,):

        os.system('cls')

        # Regresa los colores a la normalidad
        print("\033[0;37;48m \033[0;37;48m")

        print('\u001b[33;1m\t\t\t\t\t\t\tProyecto Final de Matemáticas I')
        print(
            '\n\n\u001b[36m\t\t1-Matrices\t\t2-Funciones\t\t3-Límites\t\t4-Derivadas\t\t5-Aplicaciones de la derivada\t\t6-Salir')
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
