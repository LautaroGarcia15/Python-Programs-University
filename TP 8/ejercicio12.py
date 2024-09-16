dic = {'cuaderno1':1200, 'cuaderno2':1300, 'cuaderno3':1500, 'cuaderno4':1800, 'cuaderno5':2000}
for elemento in dic:
    dic[elemento] += dic[elemento] * 0.15

print (dic)
claves = list(dic.keys())
print(claves)
mas_caro = max(dic.items(), key=lambda x: x[1])
print(mas_caro)
