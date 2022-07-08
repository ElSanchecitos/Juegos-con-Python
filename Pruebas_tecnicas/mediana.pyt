def mediana(lista1, lista2):
    mediana = 0
    lista3 = lista1 + lista2
    lista3 = sorted(lista3)
    if len(lista3) % 2 != 0:
        for e in lista3:
            indices = lista3.index(e)
            mitad = int(indices / 2)
            mediana = lista3[mitad]
        return mediana

    elif len(lista3) % 2 == 0:
        for i in lista3:
            indices = lista3.index(i)
            mitad = int(indices / 2)
            mediana = (lista3[mitad] + lista3[mitad+1]) / 2
        return mediana

lis1 = [1,6,4]
lis2 = [7,9,11]

print(mediana(lis1, lis2))

"""
for e in lista3:
    indices = lista3.index(e)
    mitad = int(indices / 2)
    mediana = lista3[mitad]
    #return mediana
"""

"""

lista3 = lista1 + lista2 
print(lista3)
print(sorted(lista3))

mitad_impar = len(lista3) / 2 + 0.5
print(int(mitad_impar))
"""

lista1 = [5,5,5,5,5,5]
lista2 = [6,6,6,6,6,30,40]
lista3 = lista1 + lista2 

#print(lista3)
#print(sorted(lista3))

#for ele in lista3:
#    print(lista3.index(ele))


#print(mediana(lista1, lista2))



#impar
new_list1 = [5,7,8,10,9,11,12]
new_list2 = [6,15,17,21,43,91]
new_list3 = new_list1 + new_list2
new_list3 = sorted(new_list3)
#print(new_list)


for e in new_list3:
    indices = new_list3.index(e)
    mitad = int(indices / 2)
    mediana = new_list3[mitad]
#print(mediana)

#par
new_list = [5,7,8,10,9,11,12,6,15,17,21,43]
new_list = sorted(new_list)
#print(new_list)

mitad = 0
for e in new_list:
    indices = new_list.index(e)
    mitad = int(indices / 2)
#print("Right:", new_list[mitad+1])
#print("Left:", new_list[mitad])

mediana = (new_list[mitad+1] + new_list[mitad]) / 2
#print(mediana)





new_lista1 = [1,2,4,3,11,21]
new_lista2 = [5,7,9,6,8,10,20]

#print(mediana(new_lista1, new_lista2))


#Pruebas de mediana_par
def mediana(lista1, lista2):
    mediana = 0
    lista3 = lista1 + lista2
    lista3 = sorted(lista3)
    if len(lista3) % 2 != 0:
        for e in lista3:
            indices = lista3.index(e)
            mitad = int(indices / 2)
            mediana = lista3[mitad]
        return mediana
    
    elif len(lista3) % 2 == 0:
        for i in lista3:
            indices = lista3.index(i)
            mitad = int(indices / 2)
            mediana = (lista3[mitad] + lista3[mitad+1]) / 2
        return mediana

        
new_list1 = [5,7,8,10,9,11,12,35]
new_list2 = [6,15,17,21,43,91]
new_list3 = new_list1 + new_list2
#print(sorted(new_list3))
#print(mediana(new_list1,new_list2))