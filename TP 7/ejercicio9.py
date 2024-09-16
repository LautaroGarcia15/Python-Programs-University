def imprimir_matriz(matriz, indice):
    if indice < len(matriz):
        fila = matriz[indice]
        for elemento in fila:
            print(elemento, end=" ")
        print()  # Salto de línea después de imprimir la fila
        imprimir_matriz(matriz, indice + 1)

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
indice = 0
imprimir_matriz(matriz, indice)
