#INTENTO 2
import numpy as np

def crearTablero():
    tablero = np.zeros((9,9), dtype=int)
    return tablero

def encontrarCero(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

def esValido(tablero, num, pos):
    # revisar fila
    for i in range(9):
        if tablero[pos[0]][i] == num and pos[1] != i:
            return False
    # revisar columna
    for i in range(9):
        if tablero[i][pos[1]] == num and pos[0] != i:
            return False
    # revisar cuadrado
    cuadradoX = pos[1] // 3
    cuadradoY = pos[0] // 3
    for i in range(cuadradoY*3, cuadradoY*3 + 3):
        for j in range(cuadradoX * 3, cuadradoX*3 + 3):
            if tablero[i][j] == num and (i,j) != pos:
                return False
    return True

def resolver(tablero):
    encontrar = encontrarCero(tablero)
    if not encontrar:
        return True
    else:
        fila, columna = encontrar
    for i in range(1,10):
        if esValido(tablero, i, (fila, columna)):
            tablero[fila][columna] = i
            if resolver(tablero):
                return True
            tablero[fila][columna] = 0
    return False

def imprimirTablero(tablero):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")

tablero = crearTablero()

if __name__ == "__main__":
    print("Sudoku")
    print("Tablero inicial:")
    imprimirTablero(tablero)
    resolver(tablero)
    print("Tablero solucionado:")
    imprimirTablero(tablero)