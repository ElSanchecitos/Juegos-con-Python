from audioop import reverse
from math import sqrt
from typing import Iterable


lista = ["a","b","c","d"]
cadena = "1,2,3,4,5,6,7,8,9,0"
print(cadena)
cadena_split = cadena.split(",")
cadena_remove = cadena.replace(","," ")
print(cadena_split)
print(cadena_remove)
print(cadena.find("5"))
print(len(cadena))


print(list(cadena))
print(str(lista))


#Metodo Join--> listas y metodo split-->cadenas 
demolist = ["1","2","3","4"] 
delim = "@"
new_string_join = "-".join(demolist)
print(f"Nueva string con join: {new_string_join}")
new_list_split = new_string_join.split("-")
print(f"Nueva list con split: {new_list_split}")


# Json 
import json

data = ["DisneyPlus","Netflix","Peacock"]
json_string = json.dumps(data)
print(f"data dumps: {json_string}")

array = '{"drinks": ["coffe","tea","water"]}'
data = json.loads(array)
print(f"Data loads: {data}")

for element in data["drinks"]:
    print(element)


dic = {"drinks": ["coffe","tea","coca cola"], "food": ["Hamburger", "pizza","soup"],"Nombre": ("Diego",)}
for ele in dic["drinks"]:
    print(ele)

for ele in dic["Nombre"]:
    print(ele)
    

for clave in dic.keys():
    print(clave)

for valor in dic.values():
    print(valor)

for clave,valor in dic.items():
    print(f"{clave}:{valor}")



#lambda
def num_elevados_mismos(x):
    return x*x
print(num_elevados_mismos(8))

s = lambda x:x*x
print(s(8))


def greeting():
    return "Hello"
print(greeting())

greet_me = lambda: "Hello"
print(greet_me())



#dar argumentos en lambda

strip_and_upper_case = lambda s: s.strip().upper()
# strip() --> quitar espacios en blanco
print(strip_and_upper_case("  Hello     "))


#Metodo strip
text = "     ba a a a e"
lista = []
for i in text:
    if i == " ":
        continue
    else:
        lista.append(i)
print(lista)

for i in lista:
    #print(i, end="")
    continue



#lambda en listas
my_list = [3, -4, -2, 5, 1, 7]
print(sorted( my_list, key=lambda x: abs(x)))


#Filter en iterables
print(list(filter(lambda x: x>0, my_list)))

#map en python
print(list(map(lambda x: abs(x), my_list)))
print("map")


def es_par(n):
    if n % 2 == 0:
        return True

numeros = [56,4,2,75,12,45,7,21,86]
print(list(filter(es_par, numeros)))
print(list(filter(lambda n: n % 2 == 0, numeros)))


def es_impar(n):
    if n % 2 != 0:
        return True 

print(list(filter(es_impar, my_list)))

nums = [-6,-5,1,-2,3,4,5,-1,9,-8,10]

def es_mayor_tres(n):
    if n > 3:
        return True

print(list(filter(es_mayor_tres, nums)))
print(list(filter(lambda n: n>3, nums)))

letras = ["r","a","e","t","p","i","f","o","w","u","x"]
def es_vocal(n):
    if n == "a" or n == "e" or n == "i" or  n == "0" or n == "u":
        return True    

print(list(filter(es_vocal, letras)))
print(list(filter(lambda n: n == "a" or n == "e" or n == "i" or  n == "0" or n == "u", letras)))


letras = ["r","a","e","t","p","i","f","o","w","u","x"]
def no_vocal(n):
    if n == "a" or n == "e" or n == "i" or  n == "0" or n == "u":
        return False
    else:
        return True    

print(list(filter(no_vocal, letras)))




letras = ["r","a","e","t","p","i","f","o","w","u","x"]
vocales = ["a","e","i","o","u"]


def es_vocal(letras):
    vocales = ["a","e","i","o","u"]
    
    if letras in vocales:
        return True 
    else:
        return False

def no_vocal(letras):
    vocales = ["a","e","i","o","u"]

    if letras in vocales:
        return False
    else:
        return True

print(list(filter(es_vocal, letras)))
print(list(filter(lambda letras: letras in vocales, letras)))

print(list(filter(no_vocal, letras)))
print(list(filter(lambda letras: letras not in vocales, letras)))












fruits = {
    "apples":70,
    "bananas":20,
    "oranges":100,
    "grapes":40,
    "tangerines":5,
}

ordenado = dict(sorted(fruits.items(), key=lambda x: x[1]))
print(ordenado)


#Metodos sort() and sorted()
nombres = ["Luis","Maria","Pedro","Mario","Leon","Claire"]
edades = [6,23,6,1,2,3,4]
print("Nombres originlaes: ")
print(nombres)
print("Edades originales: ")
print(edades)

#Los ordenamos: uno sort y otro con sorted para demostrar el orden inverso
nombres_ordenados = sorted(nombres, reverse=True)
edades.sort(reverse=False)

print("Nombres ordenados: ")
print(nombres_ordenados)
print("Edades ordenadas: ")
print(edades)

y = -1
print(abs(y)) # Regresa el valor absoluto --> positivo

