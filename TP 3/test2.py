def crear_matriz_zigzag(n):
    matriz = [[0] * n for _ in range(n)]
    num = 1

    for diagonal_sum in range(2 * n - 1):
        if diagonal_sum < n:
            # Diagonales superiores
            if diagonal_sum % 2 == 0:
                for i in range(diagonal_sum, -1, -1):
                    matriz[i][diagonal_sum - i] = num
                    num += 1
            else:
                for i in range(0, diagonal_sum + 1):
                    matriz[i][diagonal_sum - i] = num
                    num += 1
        else:
            # Diagonales inferiores
            if diagonal_sum % 2 == 0:
                for i in range(diagonal_sum - n + 1, n):
                    matriz[i][diagonal_sum - i] = num
                    num += 1
            else:
                for i in range(n - 1, diagonal_sum - n, -1):
                    matriz[i][diagonal_sum - i] = num
                    num += 1

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

n = 5  # Puedes cambiar este valor para obtener diferentes tamaños de matriz
matriz_zigzag = crear_matriz_zigzag(n)
imprimir_matriz(matriz_zigzag)
