

class Main():
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def select_option(self):
        print('fasf')
    
    def run(self):
        print("\033[0;37;48m \033[0;37;48m")  # Regresa los colores a la normalidad

        print('\u001b[33;1m\t\t\t\t\t\t\tProyecto Final de Matemáticas I')

        print('\n\n\u001b[36m\t\tMatrices\t\tFunciones\t\tLímites\t\tDerivadas\t\tAplicaciones de la derivada')
        print("\n\n\u001b[39m\t       (row, col)\t\t  f(x)\t\t\tLim f(x)\t  f'(x)\t\t\t\tf'(x)=🏠")

        print("\033[0;37;48m \033[0;37;48m")  # Regresa los colores a la normalidad

        self.select_option()



Main.run()