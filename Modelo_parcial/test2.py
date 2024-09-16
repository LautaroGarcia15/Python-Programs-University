paginas = int(input("Cantidad de páginas? "))
copias = int(input("Cantidad de copias? "))
conintercalacion = list(range(1, paginas+1)) * copias
sinintercalacion = sorted(conintercalacion)
print()
print("Secuencia con intercalación:", *conintercalacion)
print("Secuencia sin intercalación:", *sinintercalacion)