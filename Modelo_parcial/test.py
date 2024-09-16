def generar_matriz(N, f, c):
    tablero = [[0] * N for _ in range(N)]
    tablero[f][c] = 2
    return tablero

def cambiar_pos(tablero, f, c, moverf, moverc):
    N = len(tablero)
    movimientos = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

    if [moverf - f, moverc - c] in movimientos and 0 <= moverc < N and 0 <= moverf < N:
        tablero[moverf][moverc] = 2
        tablero[f][c] = 0
    else:
        print("Movimiento no válido")

    return tablero

def imprimir_tablero(tablero):
    N = len(tablero)

    # Imprimir números de columna
    print("   ", end="")
    for col in range(1, N + 1):
        print("%3d" % col, end="")
    print("\n")

    for i, fila in enumerate(tablero):
        print(i + 1, end="  ")
        for elemento in fila:
            print("%3d" % elemento, end="")
        print()

N = 8
f = int(input("Ingrese fila: ")) - 1
c = int(input("Ingrese columna: ")) - 1

tablero = generar_matriz(N, f, c)
imprimir_tablero(tablero)
moverf = int(input("Ingrese a dónde lo quiere mover (fila): ")) - 1
moverc = int(input("Ingrese a dónde lo quiere mover (columna): ")) - 1
tablero = cambiar_pos(tablero, f, c, moverf, moverc)
imprimir_tablero(tablero)
