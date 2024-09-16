datos = [40,20,51,41,30,11,50,31,10,21]
funcion = datos.sort(key = lambda x: x % 10 == 0, reverse=True)

print(datos)