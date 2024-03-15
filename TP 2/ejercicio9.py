def generar_lista_multiplos(A, B):
    lista = [i for i in range(A,B) if i%7 == 0 and i%5 != 0]

    return lista


A = int(input("ingrese el valor inicial: "))
B = int(input("ingrese el valor final: "))

lista_multiplos = generar_lista_multiplos(A,B)
print("La lista de multiplos es: ",lista_multiplos)