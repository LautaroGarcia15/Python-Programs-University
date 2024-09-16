file = open("E:\\Programacion 1\\Final\\compraVentaMercaderia.txt", "rt", encoding="UTF8")

def getYear(value):
  return value[6:10]

def isSale(value):
  return value[14] == ' '

def getQuantity(value, isSale):
  return int(value[11:14]) if isSale else int(value[32:35])

def getName(value, isSale):
  return value[15:35] if isSale else value[11:31]

def getPrice(value):
  return float(value[36:43])

def list_stock(stock_list):
  for i in range(len(stock_list)):
    print(f"{i + 1}. {stock_list[i][0]}: { stock_list[i][1] }")

stock = {}
ingresos = 0
egresos = 0

for index, value in enumerate(file):
  is_sale = isSale(value)
  year_operation = getYear(value)
  product_name = getName(value, is_sale)
  product_quantity = getQuantity(value, is_sale)
  product_price = getPrice(value)

  if not product_name in stock:
    stock[product_name] = 0

  if is_sale:
    if year_operation == '2009':
      ingresos += (product_price * product_quantity)

    stock[product_name] -= product_quantity
  else:
    if year_operation == '2009':
      egresos += (product_price * product_quantity)

    stock[product_name] += product_quantity

resultado_ejercicio = round(ingresos - egresos, 2)
stock_list = []

for key in stock:
  product = [key, stock[key]]
  stock_list.append(product)

stock_list.sort(key=lambda stock: stock[1], reverse=True)

print("RESULTADO EJERCICIO 2009: ", resultado_ejercicio, "\n")
list_stock(stock_list)