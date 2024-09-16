def imprimir(paginas, copias):
    lista = []
    for i in range(copias):
        for j in range(1, paginas+1):
            lista.append(j)
    return lista

paginas = int(input("ingrese cantidad de paginas: "))
copias = int(input("ingrese cantidad de copias"))

intercalada = imprimir(paginas, copias)
print(intercalada)

intercalada.sort()
print(intercalada)