def devolvermayor(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    elif num2 == mayor:
        mayor = -1
    elif num3 == mayor:
        mayor = -1
    return mayor

num1 = int(input("ingrese un numero positivo: "))
num2 = int(input("ingrese un numero positivo: "))
num3 = int(input("ingrese un numero positivo: "))

valormayor = devolvermayor(num1, num2, num3)

if valormayor >= 0:
    print("el mayor es: ",valormayor)
else:
    print ("No existe el unico mayor")