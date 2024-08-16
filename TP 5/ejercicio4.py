def impresion_numero():
    try:
        for i in range(1, 100001):
          print(i)
    except KeyboardInterrupt:
      responde = input("¿Desea detener el programa? (S/N) ")
    if responde.upper == 'S':
        print("Programa detenido.")
    else:
        for i in range(i, 100001):
          print(i)

impresion_numero()