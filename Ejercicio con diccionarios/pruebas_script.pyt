usuarios = {}


def agregar_usuario(ID,nombre, direccion, telefono):
    global usuarios
    usuarios[ID] = nombre,direccion,telefono
    return usuarios

id = 1
nom = "Diego"
dir = "calle 20"
tel = "12312312"

agregar_usuario(id, nom, dir, tel)

id = 2
nom = "Camilo"
dir = "calle 8"
tel = "3123123"

agregar_usuario(id, nom, dir, tel)



        

#
def listar_usuario(id):
    for clave,valor in usuarios.items():
        if id == clave:
            print (clave , valor)
    

listar_usuario(1)




#

#for clave,valor in usuarios.items():
    #print(clave, valor)


#for valor in usuarios.values():
#    print(valor)

#for clave in usuarios.keys():
#    print(clave)
