def numero_de_socio():
    n_socio = int(input("ingrese numero de socio de 5 digitos: "))
    lista_socios = []
    
    while n_socio > 9999 and n_socio < 100000:
        lista_socios.append(n_socio)
        
        n_socio = int(input("ingrese numero de socio: "))
    
    return lista_socios

def cantidad_de_ingresos(lista_socios):
    for socio in lista_socios:
        cantidad = lista_socios.count(socio)
        print("El socio: ", socio, "ingreso ", cantidad)

        if socio in lista_socios:
            lista_socios.remove(socio)

    return lista_socios

lista_socios = numero_de_socio()
cantidad_de_ingresos(lista_socios)


print("La lista de socios es: ", lista_socios)