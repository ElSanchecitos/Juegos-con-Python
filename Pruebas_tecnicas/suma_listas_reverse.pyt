def addTwoNumbers(l1, l2):
    resultado = []
    i = 0
    while i < len(l1):
        if l1[i] != 0 or l2[i] != 0:
            reversed_l1 = list(reversed(l1))
            cadena_l1 = ""
            for x in reversed_l1:
                if int(x):
                    cadena_l1 += str(x)

            reversed_l2 = list(reversed(l2))
            cadena_l2 = ""
            for y in reversed_l2:
                if int(y):
                    cadena_l2 += str(y)

            suma = str(int(cadena_l1) + int(cadena_l2))
            for num in suma:
                resultado.append(int(num))

            return  list(reversed(resultado))
        
        else:
            resultado = [0]
            return resultado
    
        i += 1


#l1 = [9,9,9,9,9,9,9]
#l2 = [9,9,9,9]
#l1 = [5,6,4]
#l2 = [2,4,3]
l1 = [0]
l2 = [0]

print(addTwoNumbers(l1,l2))

lista_nums= [1,2,3,4,5]
def reversa_lista(lista):
    lista_reversa = []
    i = 1
    while i <= len(lista):
        lista_reversa.append(lista[-i])
        i+= 1

    return lista_reversa


print(reversa_lista(lista_nums))


i = 0

while i < len(l1):
    if l1[i] != 0 or l2[i] != 0:
        print("pasa")
    else:
        print("No pasa")
    i += 1



"""
reversed_l1 = list(reversed(l1))
cadena_l1 = ""
for x in reversed_l1:
    if int(x):
        cadena_l1 += str(x)
print(cadena_l1)

reversed_l2 = list(reversed(l2))
cadena_l2 = ""
for y in reversed_l2:
    if int(y):
        cadena_l2 += str(y)
print(cadena_l2)

resultado = int(cadena_l1) + int(cadena_l2)
print(list(reversed(str(resultado))))
"""