#!/usr/bin/env python3
# -*- encode: utf-8 -*-
#encode/coding

usuarios = {}

def agregar_usuario():
    global usuarios
    id = int(input("Ingrese el ID: "))
    nombre = input("Ingrese el nombre: ")
    dir = input("Ingrese la dirección: ")
    tel = input("Ingrese el teléfono: ")

    usuarios[id] = nombre,dir,tel
    #print(usuarios)

def borrar_usuario(id):
    global usuarios
    del(usuarios[id])
    print("Eliminado")

"""
def listar():
    global usuarios
    for clave,valor in usuarios.items():
        print(clave, valor)
"""
def listar():
    global usuarios
    for user in usuarios:
        print(
            """
            ID: {}
            Nombre: {} 
            Dirección: {}
            Teléfono: {}
            """.format(user,usuarios[user][0],usuarios[user][1],usuarios[user][2]))


def listar_usuario(id):
    for clave,valor in usuarios.items():
        if id == clave: 
            clave, valor
        else: 
            print("No existe el usuario")
        return clave , valor



def actualizar_usuario(id):
    try: 
        for clave in usuarios.keys():
            if clave == id:
                nombre = input("Ingrese el nombre: ")
                dir = input("Ingrese la dirección: ")
                tel = input("Ingrese el teléfono: ")
                usuarios[id] = nombre,dir,tel

        print("Persona actualizada")
        print(usuarios[id])
    except Exception as e:
        print(f"Ocurrió un error {e}")


while True:
    print("""
    --------Aplicación en Python con diccionarios----------
    
    [1]------Agregar usuarios------
    [2]------Eliminar usuarios-----
    [3]------Actualizar un usuario-----
    [4]------Listar usuarios-------
    [5]------Listar un usuario-----

    [0]------Salir------

    """)

    try:
        option = int(input("Selecciona una opción: "))
        
        if option == 1:
            agregar_usuario()
        
        elif option == 2:
            id = int(input("Ingrese el ID del usuario: "))
            borrar_usuario(id)

        elif option == 3:
            id = int(input("Ingrese el ID del usuario: "))
            actualizar_usuario(id)
        
        elif option == 4:
            listar()

        elif option == 5:
            id = int(input("Ingrese el ID del usuario: "))
            print(listar_usuario(id))
            
        elif option == 0:
            exit()

        else: 
            print("No esta la opcion en el menú")
    
    except Exception as e:
        print(f"El error es {e}")
    
    