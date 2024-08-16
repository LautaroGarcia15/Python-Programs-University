def verificacion(direccion_correo):
    Valida = False

    partes = direccion_correo.split("@")
    
    if len(partes) == 2:
        usuario = partes[0]
        dominio = partes[1]
        
        if usuario.isalnum():
            
            partes_dominio = dominio.split(".") 

            if len(partes_dominio) >= 3 and partes_dominio[-1] == "ar" and partes_dominio[-2] == "com" and len(partes_dominio[-3]) > 0:
                Valida = True
                
    
    return Valida

lista = []
direccion_correo = input("ingrese un correo: ")
if verificacion(direccion_correo):
    lista.append(direccion_correo)

while direccion_correo != "":
    direccion_correo = input("ingrese un correo: ")
    if verificacion(direccion_correo) and direccion_correo not in lista:
        lista.append(direccion_correo)

lista_ordenda = sorted(lista)
print(lista_ordenda)