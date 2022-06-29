print(f"Mayor de dos numeos".center(50, "-"))
def max(a,b):
    mayor = None
    if a > b:
        mayor = a
        print(f"Mayor es a: {mayor}")
    elif b > a:
        mayor = b
        print(f"Mayor es b: {mayor}")
    else: 
        print("Los numeros son iguales")
    
    return mayor

max(2,4)

print(f"El mayor de tres numeros".center(50,"-"))

def max_de_tres(a,b,c):
    mayor = None
    if a > b and a > c:
        mayor = a
        print(f"Mayor es a: {mayor}")
    elif b > a and b > c:
        mayor = b
        print(f"Mayor es b: {mayor}")
    elif c > a and c > b:
        mayor = c
        print(f"Mayor es c: {mayor}")
    else: 
        print("Los numeros son iguales")
    
max_de_tres(2,3,1)

print(f"Longitud lista".center(50,"-"))

def len(lista):
    contador = 0

    for i in lista:
        contador += 1
    
    return contador

print(len([1,2,3,4,5,6,7,8,9,10]))

print(f"Vocales".center(50,"-"))

def vocal(letra):
    vocales = ["a","e","i","o","u"]
    booleano = None

    for vocal in vocales:
        if vocal == letra:
            booleano = True
            print(f"Si es una vocal: {letra}")
        else: 
            booleano = False
            print(f"No es una vocal: {letra}")
        
        return booleano

print(vocal("a"))

print(f"Suma de lista".center(50,"-"))

def sum(lista):
    suma_lista = 0

    for i in lista:
        suma_lista += i
    
    return suma_lista

print(sum([1,2,3,4]))

print(f"Multiplicacion".center(50,"-"))

def multip(lista):
    multip_lista = 1

    for i in lista:
        multip_lista *= i
    
    return multip_lista

print(multip([1,2,3,4]))

print(f"Invertir de cadena".center(50,"-"))

def invertida(cadena):

    resultado = cadena[::-1]

    return resultado

print(invertida("estoy probando"))

print(f"Palindromo".center(50,"-"))

def es_palindromo(cadena):
    booleano = None

    if cadena[0] == cadena[-1] and cadena[1] == cadena[-2]:
        booleano = True
        print(f"Es un palindromo: {cadena}")
    else: 
        print(f"No es un palindromo: {cadena}")
        booleano = False

    return booleano

print(es_palindromo("bob"))

"""
cadena = "radar"

print(cadena[-1])
print(cadena[-2])
print("------------------------------")
print(cadena[0])
print(cadena[1])
"""
print(f"Superposicion de listas".center(50,"-"))

def super_posicion(lista1, lista2):

    booleano = None

    for i in lista1,lista2:
        print(i)
        if i == i:
            print(i)
            booleano

    return booleano
    
#print(super_posicion([1,2,3,4,5],[7,6,8,9,10]))

def superposicion(lista1,lista2):

    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

#print(superposicion([4,5,6,7,3,9],[1,2,3]))
print(superposicion([1,4,5,6,7,34,10,9,123],[19,2,3,14,55,123,45,78,99,100]))

print(f"Generar Caracteres".center(50,"-"))

def generar_n_caracteres(entero, caracter):

    return entero * caracter

print(generar_n_caracteres(5,"x"))

print(f"Generar caracteres con una lista de numeros".center(50,"-"))

def generador_caracteres(nums):

    for i in nums:
        print(i * "*")
    
generador_caracteres([1,2,3,4,5,6])

print(f"Generar caracteres con range".center(50,"-"))

def generador_caracteres_range(limite):

    for i in range(1,limite+1):
        print(i * "*")

generador_caracteres_range(10)