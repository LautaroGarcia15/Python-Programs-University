def grabarrangoalturas():
    try:
        arch1 = open("alturas.txt", "wt")
        deporte = input("Ingresar Disciplina (Enter para terminar): ")
        while deporte != "":
            assert deporte.isalnum(), "Nombre invalido"
            arch1.write(deporte + "\n")
            altura = float(input("Ingresar altura del atleta (-1 para terminar): "))
            while altura != -1:
                arch1.write(str(altura) + "\n")
                altura = float(input("Ingresar altura del atleta (-1 para terminar): "))
            deporte = input("Ingresar Disciplina (Enter para terminar): ")
        else:
            arch1.write("...")
    except FileNotFoundError as mensaje:
        print(mensaje)
    except OSError as mensaje:
        print(mensaje)
    except AssertionError as mensaje:
        print(mensaje)
    finally:
        try:
            arch1.close()
        except NameError:
            pass
                
def grabarpromedio():
    skip = True
    suma = 0
    cantidad = 0        
    try:
        arch1 = open("alturas.txt", "rt")
        arch2 = open("promedio.txt", "wt")
        for linea in arch1:
            linea = linea.rstrip("\n")
            if skip == True:
                arch2.write(linea + '\n')
                skip = False  
            elif linea.isalpha() or linea == "...":
                promedio = suma / cantidad
                arch2.write(f"{promedio}" + '\n')
                if linea != "...":
                    arch2.write(linea + "\n")
                suma = 0
                cantidad = 0
            else:
                suma += float(linea)
                cantidad += 1
    except FileNotFoundError as mensaje:
        print(mensaje)
    except OSError as mensaje:
        print(mensaje)
    finally:
        try:
            arch1.close()
            arch2.close()
        except NameError:
            pass    

def mostrarmasaltos():
    suma = 0
    cantidad = 0
    try:
        arch2 = open("promedio.txt", "rt")
        for linea in arch2:
            linea = linea.rstrip('\n')
            if not linea.isalpha():
                suma += float(linea)
                cantidad += 1
        promedio = suma / cantidad
        print(f"El promedio general es de {promedio}m")
        arch2.seek(0)
        for linea in arch2:
            linea = linea.rstrip('\n')
            if linea.isalpha():
                deporte = linea
            else:
                if float(linea) > promedio:
                    print(f"La disciplina {deporte} supera el promedio general.")          
    except FileNotFoundError as mensaje:
        print(mensaje)
    except OSError as mensaje:
        print(mensaje)
    finally:
        try:
            arch2.close()
        except NameError:
            pass            

# Programa Principal
grabarrangoalturas()
grabarpromedio()    
mostrarmasaltos()
