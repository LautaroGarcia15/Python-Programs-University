def cadena_capicua(frase):
    flag = True
    for i in range((len(frase))//2):
        if frase[i] != frase[len(frase) -i -1]:
            flag =  False
        
    return flag
    

frase = input("Ingrese una cadena de caracteres: ")

if cadena_capicua(frase):
    print("Es capicua")
else:
    print("No es capicua")