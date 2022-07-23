def primos(limite):
    primos_list = []
    contador = 0
    for numero in range(1, limite+1):
        for divisor in range(limite, 0, -1):
            if numero%divisor == 0:
                contador +=1
        if contador == 2:
            print("Es un número primo", numero)
            primos_list.append(numero)
            contador = 0
        else:
            print("No es un número primo", numero)
            contador = 0
    return primos_list

print(primos(11))

cont = 0
lista_primos = []
for numero in range(2, 11):
    for divisor in range(10, 0, -1):
        #print(numero, divisor)
        if numero%divisor == 0:
            cont = cont + 1
    if cont == 2:
        #print("Es primo:", numero)
        cont = 0
        lista_primos.append(numero)
    else:
        #print("No es primo:", numero)
        cont = 0
        
print(lista_primos)
