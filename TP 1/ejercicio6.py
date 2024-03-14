def juntarnumeros(num1,num2):
    numaux = num2
    while numaux > 0:
        num1 *= 10
        numaux //= 10
    return num1 + num2 


num1 = int(input("ingrese un numero positivo: "))
num2 = int(input("ingrese otro numero positivo: "))

juntos = juntarnumeros(num1,num2)
print(juntos)