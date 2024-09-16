cadena = input("Ingrese una cadena que contenga una direccion de correo: ")

partes = cadena.split('@')

if len(partes) != 2:
    print("La cadena ingresada no contiene una dirección de correo válida.")
        
    
usuario = partes[0].split()[-1]
dominio = partes[1].split()[0]
tupla = tuple(usuario)

print("Usuario:", usuario)
print("Dominio:", dominio)
print(tupla)
