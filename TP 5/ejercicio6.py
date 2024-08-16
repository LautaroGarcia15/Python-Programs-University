def numeros():
    lista = []
    numero = int(input("ingrese numero para meter en la lista (Ingrese -1 para finalizar): "))

    while numero != -1:
        lista.append(numero)
        numero = int(input("ingrese numero para meter en la lista: "))
    
    return lista

def pertenece(lista):
    while True:
        try:
            pos = lista.index(int(input("ingrese la posicion que quiere ver: ")))
            print("La posicion es: ", pos)
            break

        except ValueError:
            print("El valor no esta en la lista. ")
        print("Intente nuevamente. ")


lista = numeros()
pertenece(lista)    