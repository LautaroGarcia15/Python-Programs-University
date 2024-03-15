def normalizar_lista(lista):
    suma_total = sum(lista)
    lista_normalizada = []

    for elemento in lista:
        valor_normalizado = elemento / suma_total
        lista_normalizada.append(valor_normalizado)

    return lista_normalizada


lista_original = [1, 2]
lista_normalizada = normalizar_lista(lista_original)

print("Lista original:", lista_original)
print("Lista normalizada:", lista_normalizada)