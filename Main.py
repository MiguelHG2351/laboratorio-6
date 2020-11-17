import os
from time import sleep
# from sympy.printing import printer


class Main():

    def select_option(self, select):
        print('')
        sleep(1)
        self.run()

    def run(self,):

        os.system('cls')

        # Regresa los colores a la normalidad
        print("\033[0;37;48m \033[0;37;48m")

        print('\u001b[33;1m\t\t\t\t\t\t\tProyecto Final de Matemáticas I')
        hola = 4
        print(
            '\n\n\u001b[36m\t\tMatrices\t\tFunciones\t\tLímites\t\tDerivadas\t\tAplicaciones de la derivada')
        print(
            "\n\n\033[0;37;48m\t       (row, col)\t\t  f(x)\t\t\tLim f(x)\t  f'(x)\t\t\t\tf'(x)=🏠\033[0;37;48m")

        # Regresa los colores a la normalidad
        print("\033[0;37;48m \033[0;37;48m")

        select = 0
        try:
            select = int(input('\u001b[36m\n\t\tSelecciona que quieres hacer: \u001b[32m'))
            self.select_option(select)
        except ValueError:
            print('\u001b[31;1m\t\t>>> Error de opciones, se ingreso un tipo de dato diferente al requerido')
            # Regresa los colores a la normalidad
            print("\033[0;37;48m \033[0;37;48m")
            sleep(1)
            self.run()


Main().run()
