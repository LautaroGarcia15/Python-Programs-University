def con_intercalacion(hojas,copias):
    lista = []
    for i in range(0, copias):
        for j in range(1, hojas+1):
            lista.append(j)

    return lista
 
hojas = int(input("ingrese la cantidad de hojas del trabajo: "))
copias = int(input("ingrese la cantidad de copias que desea imprimir: "))

con_int = con_intercalacion(hojas,copias)
sin_int = sorted(con_int)

print("La secuencia impresa con intercalacion: ", con_int)
print("La secuencia impresa sin intercalacion: ", sin_int)

print("----------------------------------------------------------------")

con_inter = list(range(1, hojas+1))* copias
sin_intercalacion = sorted(con_inter)

print("La secuencia impresa con intercalacion: ", con_inter)
print("La secuencia impresa sin intercalacion: ", sin_intercalacion)