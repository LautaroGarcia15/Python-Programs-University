import random

def generar_listas():
    lista_aleatoria = [random.randint(1,100) for i in range(0,50)]

    lista_impares = [i for i in lista_aleatoria if i%2 != 0]

    return lista_aleatoria, lista_impares

lista_primera, lista_segunda = generar_listas()

print("La lista con los valores aleatorios es: ",lista_primera)
print("la lista con los valores impares es: ", lista_segunda)    