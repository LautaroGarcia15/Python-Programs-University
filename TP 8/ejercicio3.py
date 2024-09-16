cadena = input("Ingrese una cadena que contenga una dirección de correo: ")

palabras = cadena.split()

for palabra in palabras:
    if '@' in palabra:
        correo = palabra.split('@')
        if len(correo) == 2:
            dominio_parts = correo[1].split('.')
            subdominio = dominio_parts[:-1]
            dominio = dominio_parts[-1]
            resultado = (correo[0], *subdominio, dominio)
            print(resultado)
