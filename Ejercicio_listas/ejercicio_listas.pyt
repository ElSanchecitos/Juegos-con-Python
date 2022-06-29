"""
print("Parte 1: Añadir de pila1 a pila2 en orden descendente".center(50,"-"))

pila1 = [4,5,6,8]
pila2 = []


#Invertir una lista
print(pila1[::-1])
pila2.append(pila1[::-1])
print(pila2)


#Solucion
for i in pila1[::-1]:
    print(i)
    pila2.append(i)
print(pila2)



#otra formas de invertir listas
def invertir_lista(lista):
    lista_invertida = []
    cuenta = len(lista)-1
    while cuenta>= 0:
        lista_invertida.append(lista[cuenta])
        cuenta-=1
    return lista_invertida

print(invertir_lista([4,5,6,7]))    

"""

#"""



from random import random


print("Parte 2: Concatenar dos listas")
pila1 = [4,5,6,8]
pila2 = [1,2,3,9]

pila_concatenada = pila1 + pila2
#pila_concatenada = sorted(pila_concatenada, reverse=True)
#pila_concatenada = sorted(pila_concatenada)
#pila_concatenada.sort(reverse=True)
print(pila_concatenada)
#"""
