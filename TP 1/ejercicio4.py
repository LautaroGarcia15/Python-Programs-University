def billetes(compra, abonado):

    billete1 = 0
    billete2 = 0
    billete3 = 0
    billete4 = 0
    billete5 = 0
    billete6 = 0
    billete7 = 0
    vuelto = abonado - compra

    while vuelto > 0:
        if vuelto >= 500:
            billete1 += 1
            vuelto -= 500

        elif vuelto >= 100:
            billete2 += 1
            vuelto -= 100

        elif vuelto >= 50:
            billete3 += 1
            vuelto -= 50

        elif vuelto >= 20:
            billete4 += 1
            vuelto -= 20

        elif vuelto >= 10:
            billete5 += 1
            vuelto -= 10

        elif vuelto >= 5:
            billete6 += 1
            vuelto -= 5

        else:
            billete7 += 1
            vuelto -= 1

    return billete1, billete2, billete3, billete4, billete5, billete6, billete7


compra = int(input("ingrese el precio de la compra: "))
abonado = int(input("ingrese el billete con el que se realizo la compra: "))

billetes_vuelto = billetes(compra, abonado)

print("Billetes y monedas de vuelto:")
print("Billete de 500: ", billetes_vuelto[0])
print("Billete de 100: ", billetes_vuelto[1])
print("Billete de 50: ", billetes_vuelto[2])
print("Billete de 20: ", billetes_vuelto[3])
print("Billete de 10: ", billetes_vuelto[4])
print("Billete de 5: ", billetes_vuelto[5])
print("Moneda de 1: ", billetes_vuelto[6])