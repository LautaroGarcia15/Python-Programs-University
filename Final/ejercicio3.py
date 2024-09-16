def listado_stock():
    try:
        archivo = open("E:\\Programacion 1\\Final\\compraVentaMercaderia.txt", "rt", encoding="UTF8")
        diccionario_compra = {}
        diccionario_venta = {}
        resultado = 0

        for linea in archivo:
            if linea[11:14].isalpha():  # Compra
                producto_compra = linea[11:31].strip()
                stock_compra = int(linea[32:35])
                diccionario_compra[producto_compra] = stock_compra
                
                if linea[6:10] == '2009':
                    resultado =  resultado - (float(linea[36:42])*stock_compra)
                
            else:  # Venta
                producto_venta = linea[15:36].strip()
                stock_venta = int(linea[11:14])
                diccionario_venta[producto_venta] = stock_venta

                if linea[6:10] == '2009':
                    resultado = resultado + (float(linea[36:42])*stock_venta)
        
        stock = stock_total(diccionario_compra,diccionario_venta)
        print("STOCK TOTAL: ")
        for producto, cant in stock.items():
            print(str(producto)+':'+str(cant))
        
        print("El resultado por el año 2009 es: ", resultado)

    finally:
        archivo.close()

def stock_total(diccionario_compra,diccionario_venta):
    stock_productos = {}
    for elemento in diccionario_compra:
        stock_compra = diccionario_compra.get(elemento)
        stock_venta = diccionario_venta.get(elemento)
        stock_total = int(stock_compra) - int(stock_venta)

        stock_productos[elemento] = stock_total
    
    stock_productos = dict(sorted(stock_productos.items(), key = lambda x:x[1], reverse=True))
        
    return stock_productos

# Llamada a la función
listado_stock()
