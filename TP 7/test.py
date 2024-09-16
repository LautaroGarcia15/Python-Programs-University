def sumar_matriz(matriz, fila, columna):
    if fila == len(matriz):
        return 0  # Caso base: hemos llegado al final de la matriz
    elif columna == len(matriz[fila]):
        # Hemos llegado al final de la fila actual, llamamos recursivamente para la siguiente fila
        return sumar_matriz(matriz, fila + 1, 0)
    else:
        # Sumar el elemento actual y llamar recursivamente para el siguiente elemento en la misma fila
        return matriz[fila][columna] + sumar_matriz(matriz, fila, columna + 1)

# Ejemplo de uso
matriz_ejemplo = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

resultado_suma = sumar_matriz(matriz_ejemplo, 0, 0)
print("La suma de todos los elementos de la matriz es:", resultado_suma)

