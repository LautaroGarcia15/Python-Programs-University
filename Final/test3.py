def calcular_articulos():
    try:
        archivo = open("E:\\Programacion 1\\Final\\articulos.CSV", "rt")
        diccionario_mayor = {}
        diccionario_menor = {}
        diccionario_promedio = {}

        for linea in archivo:
            datos = linea.strip().split(';')

            codigo = datos[0]
            descripcion = datos[1]
            localidad = datos[2]
            provincia = datos[3]
            precio = datos[4]

            if codigo not in diccionario_mayor or int(diccionario_mayor[codigo][0]) < int(precio): #verificacion mayor
                diccionario_mayor[codigo] = [precio,localidad,provincia,descripcion]
                
            if codigo not in diccionario_menor or int(diccionario_menor[codigo][0]) > int(precio): #verificacion menor
                diccionario_menor[codigo] = [precio,localidad,provincia,descripcion]
            
            if codigo not in diccionario_promedio:
                diccionario_promedio[codigo] = [int(precio), 1, descripcion]
            
            else:
                diccionario_promedio[codigo][0] += int(precio)
                diccionario_promedio[codigo][1] += 1
        
        diccionario_mayor_ordenado = dict(sorted(diccionario_mayor.items(), key = lambda x: x[1][3]))
        diccionario_menor_ordenado = dict(sorted(diccionario_menor.items(), key= lambda x : x[1][3]))
        diccionario_promedio_ordenado = dict(sorted(diccionario_promedio.items(), key= lambda x: x[1][2]))

        print()
        print("PRECIOS MAXIMOS POR PRODUCTO: ")
        for producto in diccionario_mayor_ordenado:
            print("Producto: ", producto, ", Precio: ",diccionario_mayor_ordenado[producto][0], ", Localidad: ", diccionario_mayor_ordenado[producto][1], ", Provincia: ", diccionario_mayor_ordenado[producto][2])
        imprimir_precio_mayor(diccionario_mayor_ordenado)


        print()
        print("PRECIOS MINIMOS POR PRODUCTO: ")
        for producto in diccionario_menor_ordenado:
            print("Producto: ", producto, ", Precio: ",diccionario_menor_ordenado[producto][0], ", Localidad: ", diccionario_menor_ordenado[producto][1], ", Provincia: ", diccionario_menor_ordenado[producto][2])
        imprimir_precio_menor(diccionario_menor_ordenado)

        print()
        print("PRECIO PROMEDIO POR PRODUCTO")
        imprimir_precio_promedio(diccionario_promedio_ordenado)

            
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except OSError as mensaje:
        print("Error: ", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass

def imprimir_precio_promedio(diccionario_promedio, indice=0):
    if indice < len(diccionario_promedio):
        producto = list(diccionario_promedio.keys())[indice]
        precio_total = diccionario_promedio[producto][0]
        cantidad = diccionario_promedio[producto][1]
        precio_promedio = precio_total / cantidad

        print("Poducto: ", producto, ", Precio promedio: ", precio_promedio)

        imprimir_precio_promedio(diccionario_promedio, indice + 1)

def imprimir_precio_menor(diccionario_menor_ordenado, indice = 0):
    if indice < len(diccionario_menor_ordenado):
        producto = list(diccionario_menor_ordenado.keys())[indice]
        precio = diccionario_menor_ordenado[producto][0]
        localidad = diccionario_menor_ordenado[producto][1]
        provincia = diccionario_menor_ordenado[producto][2]

        print("Poducto: ", producto, ", Precio minimo: ", precio, localidad,provincia)
        imprimir_precio_menor(diccionario_menor_ordenado, indice + 1)

def imprimir_precio_mayor(diccionario_mayor_ordenado, indice = 0):
    if indice < len(diccionario_mayor_ordenado):
        producto = list(diccionario_mayor_ordenado.keys())[indice]
        precio = diccionario_mayor_ordenado[producto][0]
        localidad = diccionario_mayor_ordenado[producto][1]
        provincia = diccionario_mayor_ordenado[producto][2]

        print("Poducto: ", producto, ", Precio minimo: ", precio, localidad,provincia)
        imprimir_precio_mayor(diccionario_mayor_ordenado, indice + 1)


calcular_articulos()
