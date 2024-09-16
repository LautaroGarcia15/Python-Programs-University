def resto(num1, num2):
    if num2 == 0:
        return "Error: El divisor no puede ser cero."

    elif num1 > num2:
        num1 -= num2
        return resto(num1, num2)
    else:
        return num1

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

resultado = resto(num1, num2)
print(resultado)
