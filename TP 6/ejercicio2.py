import random

def lluvia():
    try:
        registro = open("Lluvias.txt", "wt")
        cantidad = random.randint(50, 200)
        dias_utilizados = []  # Para almacenar los días y meses ya utilizados

        for i in range(0, cantidad):
            # Generar un día y mes únicos
            while True:
                dia = random.randint(1, 31)
                mes = random.randint(1, 12)
                if (dia, mes) not in dias_utilizados:
                    break  # Salir del bucle si el día y mes son únicos

            precipitaciones = random.randint(0, 350)
            dias_utilizados.append((dia, mes))  # Agregar el día y mes a la lista

            registro.write(f"{dia};{mes};{precipitaciones}\n")

        print("Archivo creado correctamente.")

    except OSError as mensaje:
        print("No se pudo grabar el archivo:", mensaje)
    finally:
        try:
            registro.close()
        except NameError:
            pass

def generar_matriz():
    try:
        matriz = [[0]*12 for i in range(0,31)]
        lluvia = open('Lluvias.txt', 'rt')
        for linea in lluvia:
            datos = linea.strip().split(';')
            dia = datos[0]
            mes = datos[1]
            precipitaciones = datos[2]
            matriz[int(dia)-1][int(mes) -1] = precipitaciones

        return matriz

    except OSError as mensaje:
        print("No se pudo grabar el archivo: ", mensaje)
    finally:
        try:
            lluvia.close()
        except NameError:
            pass
        
def imprimir_matriz(matriz):
    for i,fila in enumerate(matriz):
        print(i+1, end=" ")
        for elemento in fila:
            print("%8d" %int(elemento), end="")
        print()

lluvia()
matriz =  generar_matriz()
imprimir_matriz(matriz)