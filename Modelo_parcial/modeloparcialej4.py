def generar_lista(N):
    lista = [i for i in range(1,N) if i%10 == 7 or i%7 == 0]

    return lista

def ordenar_lista(num):
    suma = 0
    while num > 0:
        suma += (num % 10)
        num = num // 10

    return suma

N = int(input("Ingrese un numero para el rango: "))

lista = generar_lista(N)
print(lista)
lista.sort(key=ordenar_lista)
print(lista)