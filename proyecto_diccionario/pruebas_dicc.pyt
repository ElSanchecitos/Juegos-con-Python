
id = 0
dicc = {}


def read_registros():
    try:
        if dicc == {}:
            print("El diccionario no tiene ningún elemento")
        else: 
            for key, value in dicc.items():
                print(f"{key} - {value}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

def read_un_registro(id_posicion):
    try:
        if dicc == {}:
            print("El diccionario no tiene ningún elemento")
        else: 
            for key,value in dicc.items():
                if key == id_posicion:
                    print(f"{key} - {value}")
                else:
                    print("El usuario no existe")
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
        if dicc == {}:
            print("El diccionario no tiene ningún elemento")
        else:
            elementos_lista = []
            lista = list(dicc.items())
            
            for ele in lista:
                list_ele = list(ele)
                elementos_lista.append(list_ele)
            
            #Cambios de datos
            print("Proporcione los nuevos datos: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido  = input("Ingrese el nuevo apellido: ")
            edad = int(input("Ingrese la nueva edad: "))
            actualizado_ele = [id_posicion, {"Nombre":nombre,"Apellido": apellido, "Edad": edad}]
            elementos_lista.append(actualizado_ele)
            dicc = dict(elementos_lista)
            print(f"Usuario actualizado: {dicc[id_posicion]}")
            return dicc

    except Exception as e:
        print(f"Ocurrio un error: {e}")

def delete_registro(id_posicion):
    try:
        if dicc == {}:
            print("El diccionario no tiene ningún elemento")
        else:
            print(f"Usuario eliminado: {dicc[id_posicion]}")
            del(dicc[id_posicion])
    except Exception as e:
        print(f"Ocurrió un error: {e}")


#Menu principal
def menu_principal():

    opcion = None
    while opcion != "0":
        print("""
            (1)-----Leer Registros-----
            (2)-----Leer Registro-----
            (3)-----Agregar Registro-----
            (4)-----Actualizar Registro-----
            (5)-----Eliminar Registro-----
            (0)-----Salir-----
        """)
        opcion = input("Ingrese una opcion (de 0 a 5): ")

        if opcion == "1":
            read_registros()

        elif opcion == "2":
            id_create = int(input("Proporcione el id del usuario: "))
            read_un_registro(id_create)

        elif opcion == "3":
            nam = input("Porporcione el nombre del usuario: ")
            surname = input("Porporcione el apellido del usuario: ")
            year = int(input("Porporcione la edad del usuario: "))
            create_registro(nam, surname, year)

        elif opcion == "4":
            id_update =  int(input("Proporcione el id del usuario: "))
            update_registro(id_update)
            
        elif opcion == "5":
            id_delete =  int(input("Proporcione el id del usuario: "))
            delete_registro(id_delete)
        
    else:
        print("Gracias por estar aqui. Feliz día")

cde = "Proporcione los nuevos datos"


if __name__ == "__main__":
    #menu_principal()
    print(len(cde)+2)