def sumar_primeros(numero, N, suma):
    if N > 0:
        if numero > 0:
            ultimo_digito = numero % 10
            suma = suma + ultimo_digito
            return sumar_primeros(numero // 10, N - 1, suma)
        else:
            return "Número ingresado tiene menos de", N, "dígitos."
    else:
        return suma

numero = int(input("Ingrese un número natural: "))
N = int(input("Ingrese la cantidad de dígitos que desea sumar: "))
suma = 0
resultado = sumar_primeros(numero, N, suma)
print("La suma de los primeros", N, "dígitos es:", resultado)
