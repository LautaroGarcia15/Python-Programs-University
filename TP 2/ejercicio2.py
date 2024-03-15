import random

def generar_lista():
    lista = []

    for i in range(0,50):
        lista.append(random.randint(1,100))

    return lista

def elemento_repetido(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True  
    return False

def sin_elementos_repetidos(lista):
    lista_sin_repetidos = []
    for i in range(len(lista)):
        if lista[i] not in lista_sin_repetidos:
            lista_sin_repetidos.append(lista[i])
    
    return lista_sin_repetidos
            

lista = generar_lista()
print("La lista es: ", lista)

repetido = elemento_repetido(lista)
print(repetido)

lista_sin_repetidos = sin_elementos_repetidos(lista)
print("La lista sin repetidos es: ", lista_sin_repetidos)