def combinadores(numero: int):
    lista_combinada = []
    lista_combinada_2 = []
    for num in range(0, numero+1):
        for i in range(numero, 1, -1):
            print("Numero_normal:", num, "-", "Rango_inverso:", i)
            if i+num == numero:
                lista_combinada.append(i)
                lista_combinada.append(num)
            # elif i+i+num == numero:
            #     lista_combinada_2.append(i)
            #     lista_combinada_2.append(num)
    return lista_combinada

print(combinadores(4))