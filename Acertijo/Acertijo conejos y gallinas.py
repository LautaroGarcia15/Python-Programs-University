'''He contado 35 cabezas y 94 patas entre las gallinas y conejos de mi granja. 
¿Cuantos conejos y cuantas gallinas tengo?'''

cabezas = 35
patas = 94

for conejos in range(cabezas+1):
    gallinas = cabezas - conejos
    if (4 * conejos + 2 * gallinas) == patas:
        print("la cantidad de conejos es : ",conejos)
        print("la cantidad de gallinas es : ",gallinas)



