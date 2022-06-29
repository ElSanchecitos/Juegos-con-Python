#Invertir Cadena 
cadena = "hola"
palabra_invertida_lista = []
print(len(cadena))

i = 1
while i <= len(cadena):
    #palabra_invertida_lista.append(cadena[-i])
    #palabra_invertida_str = cadena[-i]
    i += 1
#print(palabra_invertida_str)
#print(palabra_invertida_lista)



#Plalindromo

palabra = "ojo"


i = 1
while i <= len(palabra):
    #if palabra[-i] == palabra[i]:
        #print("Es un palindromo")
    #else:
    #    print("No es un palindromo")
    i += 1

#Recorrer lista
lista = ["a","b","c","d"]

i = 0

while i < len(lista):
    print(lista[i])
    i += 1

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