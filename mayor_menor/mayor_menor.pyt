"""
def mayor_menor(lista_numeros):
    mayor = 0
    menor = None

    #Número mayor
    for i in lista_numeros:
        if mayor == 0:
            mayor = i
        elif i > mayor: 
            mayor = i
        
    #Número menor 
    for i in lista_numeros:
        if menor is None:
            menor = i
        elif i < menor:
            menor = i
    
    resultado = f"Menor: {menor} ::: Mayor: {mayor}" 
    
    return resultado
"""
if __name__ == "__main__":
    pass
    #print(mayor_menor(lista_numeros=[3,4,5,6,7,8,1,100]))


lista_numeros = []
mayor = None
menor = None

try:
    opcion = ""
    while opcion != "D":
        opcion = input("Ingrese la opcion (D) DONE para salir or (C) CONTINUE para continuar: ")
        if opcion is "C":
            numero = int(input("Ingrese un número: "))
            lista_numeros.append(numero)
        else:
            opcion = "D"

    #Numero mayor
    for num in lista_numeros:
        if mayor is None:
            mayor = num
        elif mayor > num:
            mayor = num
    print(f"Número Mayor: {mayor}")

    #Numero menor 
    for num in lista_numeros:
        if menor is None:
            menor = num
        elif menor < num:
            menor = num
    print(f"Número Menor: {menor}")

except Exception as e:
    print(f"Ocurrió un error {e}")
    numero = 0



