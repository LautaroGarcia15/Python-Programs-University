numero = int(input("Ingrese un numero entero entre 0 y 9 (ingrese -1 para finalizar): "))
conjunto = {0,1,2,3,4,5,6,7,8,9}
while numero != -1:
    try:
        conjunto.remove(numero)
        print("El numero se removio correctamente.")
        print(conjunto)

    except KeyError:
        print("Ese numero no se encuentra en el conjunto.")
    
    numero = int(input("Ingrese un numero entero entre 0 y 9 (ingrese -1 para finalizar): "))
        
