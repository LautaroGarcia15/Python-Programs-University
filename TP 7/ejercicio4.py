def producto(num1, num2, resultado):
    if num2 != 0:
        resultado += num1
        return producto(num1, num2 - 1, resultado)
    else:
        return resultado

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
resultado = 0
productos = producto(num1, num2, resultado)
print ("El producto entre", num1,"y",num2,"es: ", productos)