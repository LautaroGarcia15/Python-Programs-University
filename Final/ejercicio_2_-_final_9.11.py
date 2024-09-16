# Función lambda que verifica si un número es triangular
es_triangular = lambda n: any(n == x * (x + 1) // 2 for x in range(1, n+1))

# Probar la función con algunos ejemplos
numero = int(input("Ingrese un numero: "))
print(es_triangular(numero))  