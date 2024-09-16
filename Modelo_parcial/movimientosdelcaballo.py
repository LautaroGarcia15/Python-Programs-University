def generar_matriz(N,f,c):
    tablero = [[0]*N for f in range(N)]
    tablero[f][c] = 2
    return tablero

def cambiar_pos(f,c, moverf, moverc):

    movimientos = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

    if [moverf - f, moverc - c] in movimientos and 0 <= moverc < N and 0 <= moverf < N:
        tablero[moverf][moverc] = 2
        tablero[f][c] = 0
        
    else:
        print("movimiento no valido")

    return tablero

def imprimir_tablero(tablero,N):
    print("  ", end="")
    for c in range(1, N+1):
        print("%3d" %c, end="")
    print()

    for i,fila in enumerate(tablero):
        print(i+1, end=" ")
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

N = 8
f = int(input("ingrese fila: "))
c = int(input("ingrese columna: "))


tablero = generar_matriz(N,f,c)
imprimir_tablero(tablero,N)
moverf = int(input("ingrese a donde lo quiere mover:"))
moverc = int(input("ingrese a donde lo quiere mover:"))
tablero = cambiar_pos(f,c, moverf, moverc)
imprimir_tablero(tablero,N)