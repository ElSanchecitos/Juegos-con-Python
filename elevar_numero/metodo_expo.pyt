def elevar(num1, num2):
    num_elevado = 1
    for i in range(1,num2+1):
        num_elevado*=num1
    return num_elevado

print(elevar(4,4))