import numpy as np
import random
##

class Minesweeper:

    def __init__(self):
        self.filas = int(input("Entre el numero de filas del tablero: "))
        self.columnas = int(input("Entre el numero de columnas del tablero: "))
        self.minas = int(input("Entre el numero de minas: "))
        self.grid = self.armar_grid(self.filas,self.columnas,self.minas)
        self.tablero = self.armar_tablero(self.grid)

    def __del__(self):
        print("Perdio el juego")
    
    def armar_grid(self,filas,columnas,minas):
        grid_minas = np.zeros(shape=(filas,columnas))
        random.seed()
        pos_minas = [ ( random.randint(0, filas-1), random.randint(0, columnas-1) ) for el in range(minas) ]
        #print(pos_minas)
        for el in pos_minas:
            grid_minas[el[0]][el[1]] = 1
        #print(grid_minas)

    def armar_tablero(self,grid):
        tablero = grid
        tablero[tablero >= 0] = '.'
        return tablero

    def seleccionar_celda(self):
        x = int(input("Selecciona la fila de la celda: "))
        y = int(input("Selecciona la columna de la celda: "))
        accion = input("Selecciona la accion a tomar: ").upper()

        if accion == 'M':
            self.marcar_celda(x,y)
        elif accion == 'U':
            self.destapar_celda(x,y)
        else:
            print("Entre M para marcar o U para Destapar")

    def destapar_celda(self,x,y):
        if self.grid[x][y] == 1:
            del buscaminas
        else:
            minas_adyacentes = self.contar_adyacentes(x,y)
            if minas_adyacentes == 0:
                for el in matriz_adyacencia:
                    self.tablero[el[0]][el[1]] = '_' 
            else:
                self.tablero[x][y] = minas_adyacentes
    
    def contar_adyacentes(self,x,y):
        bombas = 0
        if self.grid[x-1][y] == 1:
            bombas += 1
        elif self.grid[x][y-1] == 1:
            bombas += 1
        elif self.grid[x-1][y-1] == 1:
            bombas +=1
        elif self.grid[x+1][y] == 1:
            bombas +=1
        elif self.grid[x][y+1] == 1:
            bombas +=1
        elif self.grid[x+1][y+1] == 1:
            bombas +=1
        elif self.grid[x+1][y-1] == 1:
            bombas +=1
        elif self.grid[x-1][y+1] == 1:
            bombas +=1
        
        return bombas

    def marcar_celda(self,x,y):
        print('hola')


buscaminas = Minesweeper()
