
lista1 = ["Hola","a","Todos","Amigos","y","Amigas"]
lista2 = [1,2,3,4,5,6,7]
lista3 = [12123,0,1,12,334,12312,1111]

for x in range(len(lista1)-1,-1,-1):
    if lista1[x] == "Amigas":
        print(lista1.pop(x))
#print(len(lista1))
#print(lista1)

#for y in range(20-1,-1):
#    print(y)
#for x in range(20-1,1,-1):
#    print(x)   (inicio, termina, saltos)


"""
boleano = None
for i in range(0, len(lista2)):
    if lista2[i] == lista3[i]:
        print(i)
        boleano = True
    else: 
        boleano = False

print(boleano)
"""

