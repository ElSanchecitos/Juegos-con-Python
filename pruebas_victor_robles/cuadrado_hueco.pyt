def lado_cuadrado(numero):
    lado = " "
    for i in range(numero):
        print(lado + "*" + "")

    return lado

#lado_cuadrado(4)

def invertida(cadena):
    invertida = ""
    i = 1
    while i <= len(cadena):
        invertida += cadena[-i]
        i += 1

    return invertida

def invertida_youtube(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida

    return cadena_invertida

print(invertida("Diego"))
print(invertida_youtube("Diego"))

