def baraja():
    palos = ["Oros", "Espadas", "Bastos", "Copas"]
    cartas = [f"{i}  de  {palo}" for palo in palos for i in range (1,12) ]
    print (cartas)
    
baraja()