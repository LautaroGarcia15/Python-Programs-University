def crear_lista(N):
    lista = []
    for i in range(1, N+1):
        lista.append(i**2)
    return lista

def ultimos_diez(lista):
    ultimos = []
    for i in range(len(lista) - 10, len(lista)):
        ultimos.append(lista[i])
    
    return ultimos



N = int(input("ingrese un valor N: "))
print(" ")

lista = crear_lista(N)
print("La lista es: ", lista)
print(" ")

ultimos = ultimos_diez(lista)
print("Los ultimos 10 elementos son: ",ultimos)