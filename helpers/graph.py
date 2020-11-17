from sympy import *
from matplotlib import pyplot as plt
import numpy as np

def graph(function):

    # Creamos una figura para gráficar
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Centramos sus posiciones
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')


    x = np.linspace(-2, 2) # Definimos los valores en el eje x

    def h(x):
        function(x)
    plt.plot(x)