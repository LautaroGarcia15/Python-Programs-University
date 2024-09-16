def numeros_primos(N):
    lista = []
    n = 1 
    
    while n <= N:
        divisor = 2
        while divisor < n:
            if n % divisor == 0:
                break
            divisor += 1
        else:
            lista.append(n)
        n += 1
    
    return lista

N = int(input("Ingrese N: "))
lista = numeros_primos(N)
print(lista)
