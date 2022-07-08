numeros = [1,4,6,10,100,2,7,1,90,5]

def menor(lista):
    menor = None
    for num in lista:
        if menor is None:
            menor  = num
        elif num < menor:
            menor = num

    return menor

#print(menor(numeros))

def mayor(lista):
    mayor = None
    for num in lista:
        if mayor is None:
            mayor  = num

        elif num > mayor:
            mayor = num

    return mayor

#print(mayor(numeros))
print("Lista original:", numeros)

def ordernar_lista(reversa=False, lista=None):
    if reversa is False:
        for recorrido in range(1,len(lista)):
            for posicion in range(len(lista) - recorrido):
                if lista[posicion] > lista[posicion + 1]:
                    temp = lista[posicion]
                    lista[posicion] = lista[posicion + 1]
                    lista[posicion + 1] = temp

    """
    elif reversa is True:
        for recorrido in range(1,len(lista)):
            for posicion in range(len(lista) - recorrido):
                if lista[posicion] < lista[posicion + 1]:
                    temp = lista[posicion]
                    #print(temp)
                    lista[posicion] = lista[posicion + 1]
                    #print(lista[posicion])
                    lista[posicion + 1] = temp
                    #print(lista[posicion + 1])
    """
    return lista

print(ordernar_lista(lista=numeros))
#print(ordernar_lista(lista=numeros, reversa=True))