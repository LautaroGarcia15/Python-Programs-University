def encaja(ficha1,ficha2):
    a,b = ficha1
    c,d = ficha2
    if a == c or b == d:
        return True
    else:
        return False

a = int(input("ingrese ficha: "))
b = int(input("ingrese ficha: "))
c = int(input("ingrese ficha: "))
d = int(input("ingrese ficha: "))
ficha1 = (a,b)
ficha2 = (c,d)

if encaja(ficha1,ficha2):
    print(True)
else:
    print(False)

'''-----------------------Dos opciones---------------------------'''


def encaja(ficha1,ficha2):
    a,b = ficha1

    if a in ficha2  or b in ficha2:
        return True
    else:
        return False

a = int(input("ingrese ficha: "))
b = int(input("ingrese ficha: "))
c = int(input("ingrese ficha: "))
d = int(input("ingrese ficha: "))
ficha1 = (a,b)
ficha2 = (c,d)

if encaja(ficha1,ficha2):
    print(True)
else:
    print(False)