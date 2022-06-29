"""
def numeros_mayores(nums):
    mayor = None
    lista_mayores = []

    for num in nums:
        if mayor is None:
            mayor = num
        elif num > mayor:
            mayor = num
        

    print(nums)
    primer_mayor = mayor
    lista_mayores.append(primer_mayor)

    mayor = None    

    for num in nums:
        if mayor is None:
            mayor = num
        elif num > mayor: 
            mayor = num

    segundo_mayor = mayor
    lista_mayores.append(segundo_mayor)

    return lista_mayores
"""

mayor = None
nums = [11,91,8,5,27,4,81,100,101]
lista_mayores = []

print(nums)
for num in nums:
    if mayor is None:
        mayor = num
    elif num > mayor:
        mayor = num
        lista_mayores.append(num)
        nums.remove(num)
        print(nums)
        #mayor = None
        for num in nums:
            if mayor is None:
                mayor = num
            elif num > mayor:
                mayor = num
                lista_mayores.append(num)
                nums.remove(num)
                print(nums)

            

print(lista_mayores)

#print(numeros_mayores())