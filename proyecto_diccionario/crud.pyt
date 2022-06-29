
id = 0

dicc = { 
    1: {"Nombre":"Diego", "Apellido":"Sanchez", "Edad":18},
    2: {"Nombre":"Camilo", "Apellido":"Sanchez", "Edad":24},
    3: {"Nombre":"Duvy", "Apellido":"Buitrago", "Edad":46}
}
print(dicc)

#dicc  = {}


for e in dicc[1].items():
    e = list(e)
    #print(e)
    print(e[0] )
    print(e[1])
    #new_valor = e[1] = "año"
    #print(new_valor)
#print(dicc[1])

nueva_lista = dicc.items()
#print(list(nueva_lista))
#print(dict(nueva_lista))
#persona = { 1 : ["Diego","Sanchez", 18],}
personas = [{ 1 : {"Nombre":"Diego","Apellido":"Sanchez"}}]
#print(dict(personas[0]))

"""
for key in dicc.keys():
    print(key)

for value in dicc.values():
    print(value)

for key, value in dicc.items():
    print(key, value)
"""


def read_registros():
    try:
        for key, value in dicc.items():
            print(f"{key} - {value}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

def read_un_registro(id_posicion):
    try:
        for key,value in dicc.items():
            if key == id_posicion:
                print(f"{key} - {value}")

    except Exception as e:
        print(f"Ocurrio un error: {e}")

def create_registro(nombre, apellido, edad):
    try:
        global id, dicc
        id += 1
        elementos_lista = []
        lista = list(dicc.items())
        for ele in lista:
            list_ele = list(ele)
            elementos_lista.append(list_ele)
        agregar_ele = [id, {"Nombre":nombre,"Apellido": apellido, "Edad": edad}]
        elementos_lista.append(agregar_ele)
        dicc = dict(elementos_lista)
        print(f"Usuario agregado: {agregar_ele}")
        return dicc

    except Exception as e:
        print(f"Ocurrio un error: {e}")




def update_registro(id_posicion):
    try:
        global dicc
        elementos_lista = []
        lista = list(dicc.items())
        
        for ele in lista:
            list_ele = list(ele)
            elementos_lista.append(list_ele)
        
        #Cambios de datos
        if id_posicion in dicc.keys():
            print("Proporcione los nuevos datos".center(50,"-"))
            nombre = input("Ingrese el nuevo nombre: ")
            apellido  = input("Ingrese el nuevo apellido: ")
            edad = int(input("Ingrese el nuevo nombre: "))
            actualizado_ele = [id_posicion, {"Nombre":nombre,"Apellido": apellido, "Edad": edad}]
            elementos_lista.append(actualizado_ele)
            dicc = dict(elementos_lista)
            print(f"Usuario actualizado: {dicc[id_posicion]}")
        else:
            print("El usuario no existe") 
        return dicc

    except Exception as e:
        print(f"Ocurrio un error: {e}")

def delete_registro(id_posicion):
    try:
        if id_posicion in dicc.keys():
            print(f"Usuario eliminado: {dicc[id_posicion]}")
            del(dicc[id_posicion])
        else:
            print("El usuario no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    



if __name__ == "__main__":
    #create_registro(nombre="Paola",apellido="Perez",edad=40)
    #update_registro(3)
    #read_registros()
    #read_un_registro(1)
    delete_registro(5)

