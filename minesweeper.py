import numpy as np
import random
##

class Minesweeper:

    def __init__(self):
        self.filas = int(input("Entre el numero de filas del tablero: "))
        self.columnas = int(input("Entre el numero de columnas del tablero: "))
        self.minas = int(input("Entre el numero de minas: "))
        self.armar_grid(self.filas,self.columnas,self.minas)

    def armar_grid(self,filas,columnas,minas):
        grid_minas = np.zeros(shape=(filas,columnas))
        print(grid_minas)

    
buscaminas = Minesweeper()
