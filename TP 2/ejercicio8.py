def generar_lista():
    lista_impares = [i for i in range(100,200)if i%2 != 0]

    return lista_impares

lista_impares = generar_lista()

print("La lista de impares de 100 a 200 es: ", lista_impares)
