import array
from re import sub


def solution(arrayA, arrayB):
    new_array = []
    
    for i in range(len(arrayA)):
        new_array.append(arrayA[i])
        new_array.append(arrayB[i])
        
    return sorted(new_array)

#print(solution([1,2,3], [4,5,6]))
#print(solution(["A","B","C"],["D","E","F"]))

def solution_2(arrayA, arrayB):
    new_array = arrayA + arrayB
    return new_array

#print(solution([1,2,3], [4,5,6]))
#print(solution(["A","B","C"],["D","E","F"]))




##Array de arrays en un solo array

def array_arrays(array):
    
    new_array = []
    for i in array:
        for j in i:
            new_array.append(j)

    return new_array


#Pruebas 
arrays = [[1,2],[3,4],[5,6]]
print(len(arrays))
#print(arrays[2][1])
for elementos in arrays:
    for sub_elementos  in elementos:
        #print(f"Elemento: {elementos}, Sub_elementos: {sub_elementos}")
        pass

print(array_arrays(arrays))