
nums = [1,2,3,4,5]
target = 7

for x in range(len(nums)):
    for y in range(len(nums)):
        if nums[x] + nums[y] == target:
            print(nums.index(nums[x]), nums.index(nums[y]))

for x in range(len(nums)):
    indice = nums.index(nums[x])
    #print(indice)

def two_sum(lista, target: int):
    salida = []
    for x in range(len(lista)):  
        for y in range(len(lista)):
            if lista[x] + lista[y] == target:
                salida = [lista.index(lista[x]), lista.index(lista[y]),]
    return salida

print(two_sum(nums, 7))