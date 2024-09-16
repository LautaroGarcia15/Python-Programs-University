import time
import random

def crear_avion(filas):
    if filas<= 30:
        matriz= [[0]*6 for i in range(filas)]
    else:
        matriz= [[0]*10 for i in range(filas)]
        
    return matriz

def tipo_vuelo(filas):
    if filas<= 30:
        columnas_dicc={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
    else:
        columnas_dicc={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
    
    return columnas_dicc

def asignar_asientos(columnas_dicc, matriz, filas):
    try:
        arch= open("E:\\Programacion 1\\Final\\Vuelos.txt", "rt", encoding="UTF8")
        print("Archivo abierto con exito")
        time.sleep(0.5)
        
        print("Cargando asientos:")
        print()
        time.sleep(1)
        coliciones= []
        
        for linea in arch:
            info= linea.strip().split(";")
            
            if len(info)==3:
                nombre= info[0]
                columna= columnas_dicc[info[2]]
                fila= int(info[1])
                
                if matriz[fila-1][columna]==0:
                    matriz[fila-1][columna]= 1       
                    print (f"Pasajero: {nombre} asiento: {fila},{info[2]}")
                
                elif matriz[fila-1][columna]==1:
                    coliciones.append(info)
        print()
        
        for linea2 in arch:
            info= linea.strip().split(";")
            
            if len(info)==1:
                nombre= info[0]
                columna= columnas_dicc[random.randint(0,filas)]
                fila= random.randint(0,len(matriz[0]))
                while matriz[fila-1][columna]!=0:
                    columna= columnas_dicc[random.randint(0,filas)]
                    fila= random.randint(0,len(matriz[0]))
        
        print("Imprimiendo coliciones:")
        time.sleep(1)
        print()
        
        if len(coliciones)!=0:
            for i in range (len(coliciones[0])-1):
                print(f"Nombre: {coliciones[i][0]} asiento: {coliciones[i][1]},{coliciones[i][2]}")
        else:
            print("No hubieron coliciones")
            time.sleep(0.5)
        
        print()
        print("Cargando demostracion de asientos:")
        time.sleep(1)
        print()
        
        if len(matriz[0])==6:
            columnas_letra=["A","B","C","D","E","F"]
        elif len(matriz[0])==10:
            columnas_letra=["A","B","C","D","E","F","G","H","I","J"]
        
        for i in columnas_letra:
            print(f"  {i}", end="")
        print()
        
        for f in matriz:
            for c in f:
                print("%3d" %c,end="")
            print()
            
        print("Asientos libres:")
        
        for i in range (len(matriz)):
            for j in range (len(matriz[0])):
                if matriz[i][j]== 0:
                    print(f"{i+1},{columnas_letra[j]}")
            
    except NameError:
        print("No se encontro el archivo")
    except OSError:
        print("Error al leer el archivo")
    finally:
        try:
            arch.close()
            print("Archivo cerrado con exito")
        except NameError:
            pass
        

filas=int(input("Seleccione las cantidad de filas:"))
matriz= crear_avion(filas)
columnas_dicc= tipo_vuelo(filas)
asignar_asientos(columnas_dicc,matriz, filas)