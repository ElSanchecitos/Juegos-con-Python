def numeros_menores(nums):
    menor = None
    lista_menores = []

    for num in nums:
        if menor is None:
            menor = num
        elif num < menor:
            menor = num


    print(nums)
    primer_menor = menor
    lista_menores.append(primer_menor)

    menor = None    

    for num in nums:
        if menor is None:
            menor = num
        elif num < menor: 
            menor = num

    segundo_menor = menor
    lista_menores.append(segundo_menor)

    return lista_menores

print(numeros_menores([11,3,8,5,27,4,81]))