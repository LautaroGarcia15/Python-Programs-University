def multiplicacion(N):
    dic = {i:i*N for i in range(1,13)}
    return dic

N = int(input("Ingrese un numero entero: "))
diccionario = multiplicacion(N)
print("La tabla de multipicacion del numero: ",N,"es: ",diccionario)