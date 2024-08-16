
clave_maestra = input("Ingrese la clave maestra:" )
par = ""
impar = ""
for caracter in clave_maestra:
    posicion = clave_maestra.index(caracter)
    if posicion % 2 == 0:
        par = par + caracter

    else:
        impar = impar + caracter

print (par)
print (impar)

