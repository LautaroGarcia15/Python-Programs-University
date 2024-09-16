def es_ortogonal(vector1,vector2):
    a,b = vector1
    c,d = vector2
    if (a*c)+(b*d) == 0:
        return True
    else:
        False

a = int(input("ingrese ficha: "))
b = int(input("ingrese ficha: "))
c = int(input("ingrese ficha: "))
d = int(input("ingrese ficha: "))
vector1 = (a,b)
vector2 = (c,d)

if es_ortogonal(vector1,vector2):
    print(True)
else:
    print(False)