def compra_venta ():
    try:
        archivo= open("E:\\Programacion 1\\Final\\compraVentaMercaderia.txt", "rt", encoding="UTF8")
        diccionario_compra = {}
        
        lista_compra=[]

        lista_venta =[]
        for linea in archivo:
            linea = linea.rstrip('\n')
            stock_produc = linea [11:14]
            if stock_produc.isalpha():
                lista_compra.append(linea)
            else:
                lista_venta.append(linea)

        compra= dic_compra(lista_compra)
        venta=dic_venta (lista_venta)
        stock_producto (compra,venta)
        stock_producto_2009 (compra,venta)

    except FileNotFoundError as mensaje:
        print("El archivo no se encontro", mensaje)
    except OSError as mensaje:
        print("No se puede grabar el archibo", mensaje)
    finally:
        try: 
            archivo.close()
        except NameError:
            pass

def dic_compra(compra_lista):
    dic_compra = {}
    for i in compra_lista:
        año = i[6:10]
        producto = i[11:31].strip()
        stock= i[32:35]
        dic_compra[producto]=[año,stock]

    return dic_compra
    

def dic_venta (venta_lista):
    dic_venta = {}
    for i in venta_lista:
        año = i[6:10]
        stock= i[11:14]
        producto = i[15:36].strip()
        dic_venta [producto]=[año,stock]
    
    return dic_venta
    
def stock_producto (compra,venta):
    dic_stock = {}
    for producto in compra:
        valor_venta = venta.get(producto)
        valor_compra = compra.get (producto)
        stock_venta = (valor_venta[1:])
        stock_compra = (valor_compra [1:])
        stock_total = (int(stock_compra[0])) - (int(stock_venta[0])) 
       
        dic_stock [producto] = (str(stock_total))
    
    dic_ordenado = dict(sorted(dic_stock.items(), key=lambda x: int(x[1]), reverse=True))
    print("El stock disponible es:")
    for producto, cantidad in dic_ordenado.items():
        print(f"{producto}: {cantidad}")
    print()


def stock_producto_2009 (compra,venta):
    dic_stock_2009 = {}
    for producto in compra:
        valor_venta = venta.get(producto)
        valor_compra = compra.get (producto)
        año = valor_venta[:1]
        if (int(año[0]))== 2009:
            stock_venta = (valor_venta[1:])
            stock_compra = (valor_compra [1:])
            stock_total = (int(stock_compra[0])) - (int(stock_venta[0])) 
            dic_stock_2009 [producto] = (str(stock_total))
    
    dic_ordenado = dict(sorted(dic_stock_2009.items(), key=lambda x: int(x[1]), reverse=True))
    
    print("El stock disponible en el 2009 es:")
    for producto, cantidad in dic_ordenado.items():
        print(f"{producto}: {cantidad}")
    print()

compra_venta ()