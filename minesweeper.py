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
        random.seed()
        pos_minas = [ ( random.randint(0, filas-1), random.randint(0, columnas-1) ) for el in range(minas) ]
        #print(pos_minas)
        for el in pos_minas:
            grid_minas[el[0]][el[1]] = 1
        print(grid_minas)

    
buscaminas = Minesweeper()
