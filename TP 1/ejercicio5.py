def imprimirasteriscos1(filas):
    for i in range(0,filas):
        print("**********")

def imprimirasteriscos2(filas):
    for i in range(1,filas+1):
        varible = ((i*2)*'*')
        print(varible)


fila = int(input("ingrese el numero de filas: "))
imprimirasteriscos1(fila)
print("----------------")
imprimirasteriscos2(fila)  