def encontrar_minimo(matriz, fila, columna, minimo_actual):
    if fila == len(matriz):
        return minimo_actual  # Hemos llegado al final de la matriz, devolvemos el mínimo actual
    elif columna == len(matriz[fila]):
        # Hemos llegado al final de la fila actual, llamamos recursivamente para la siguiente fila
        return encontrar_minimo(matriz, fila + 1, 0, minimo_actual)
    else:
        # Encontrar el mínimo entre el elemento actual y el mínimo actual
        if matriz[fila][columna] < minimo_actual:
            minimo_actual = matriz[fila][columna]
        
        
        # Llamar recursivamente para el siguiente elemento en la misma fila
        return encontrar_minimo(matriz, fila, columna + 1, minimo_actual)

# Ejemplo de uso
matriz_ejemplo = [[8, 2, 3],
                  [4, 5, 6],
                  [7, 1, 9]]
minimo_actual = matriz_ejemplo[0][0]
minimo_encontrado = encontrar_minimo(matriz_ejemplo, 0, 0, minimo_actual)
print("El mínimo elemento de la matriz es:", minimo_encontrado)
