def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
    
n = int(input("ingrese n: "))
m = int(input("Ingrese m: "))
funcion = ackermann(m, n)
print (funcion)