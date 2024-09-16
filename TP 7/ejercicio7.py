def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

while True:
    numero1 = int(input("Ingrese un número positivo: "))
    numero2 = int(input("Ingrese otro número positivo: "))

    if numero1 > 0 and numero2 > 0:
        break
    else:
        print("Por favor, ingrese números positivos.")

mcd_resultado = mcd(numero1, numero2)
print("El Máximo Común Divisor de", numero1, "y", numero2, "es:", mcd_resultado)
