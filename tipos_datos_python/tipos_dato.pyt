
print("Listas".center(40,"-"))

frutas=["Manzana","Naranja","Pera"]
cantidades = [1,2,3,4,5,6]
print(frutas)
print(cantidades)

"""
print("Añadir datos a una lista".center(50,"-"))

deportes = []
n  = int(input("¿Cuántos deportes?: "))
for i in range(n):
    #deporte = input("Deporte: ")
    #deportes.append(deporte)
    deportes.append(input("Deporte: "))
print(deportes)
"""

#Modificar datos de una lista  

print(frutas)

print("Reemplazar datos".center(50,"-"))
frutas[0] = "Kiwi"
print(frutas)
frutas[-1] = "Plátano"
print(frutas)
frutas[1:3] = ["Mandarina","Mango"]
print(frutas)

print("Tomando dos indices".center(50,"-"))
print(frutas[1:3])
print(frutas[-3:-1])
print(frutas[-2:])
print(frutas[:])

print("Indices Positivos".center(50,"-"))
print(frutas[0])
print(frutas[1])
print(frutas[2])

print("Indices Negativos".center(50,"-"))
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

print("Borrar los elementos con (del)".center(50,"-"))
frutas[1:3] = []
print(frutas)

del frutas[0]
print(frutas)

frutas = ["Kiwi","Plátano","Mango","Mandarina"]
frutas.remove("Mandarina")
print(frutas)

print("Insertar elementos con (insert)".center(50,"-"))
frutas[1:1] = ["Toronja", "Uva", "Higo"]
print(frutas)

frutas.insert(3,"Guayaba")
print(frutas)

print("Copiar listas".center(50,"-"))
frutas2 = frutas.copy()
print(frutas2)

frutas3 = frutas[:]
print(frutas3)

print("Borrar los elementos con (pop)".center(50,"-"))
frutas2.pop() # Mango 
print(frutas2)

frutas2.pop(2) #Uva
print(frutas2)

print("Agregar elementos con (extend)".center(50,"-"))
frutas.extend(frutas3)
print(frutas)

print("Borrar los elementos con (clear)".center(50,"-"))
frutas2.clear()
print(frutas2)

print("Ejercicio : Modificar los elementos de una lista".center(50,"-"))
r = ["A","B","C","D","E"]
for i,letra in enumerate(r):
    print(i)
    print(letra)
    r[i]= letra.lower()

print(r)

#Enumarate ejercicios
etapas = ["Sring","Summer","Fall","Winter"]
list(enumerate(etapas))
print(list(enumerate(etapas,start=1)))


"""
dato = input("Dato que quiere modificar de la lista: ")
for i in range(len(frutas)):
    print(i)
    if frutas[i] == dato:
        nuevo_dat= input("Ingrese el nuevo dato: ")
        frutas[i] = nuevo_dat

print(frutas)
"""


print("Matrices".center(40,"-"))
print("Diccionarios".center(40,"-"))
print("Set".center(40,"-"))
print("Tuplas".center(40,"-"))