import numpy as np
import random
##
filas = int(input("Entre el numero de filas del tablero: "))
columnas = int(input("Entre el numero de columnas del tablero: "))
minas = int(input("Entre el numero de minas: "))

def armar_grid(filas,columnas,minas):
    grid_minas = np.zeros(shape=(filas,columnas))
    print(grid_minas)

armar_grid(filas,columnas,minas)
    
