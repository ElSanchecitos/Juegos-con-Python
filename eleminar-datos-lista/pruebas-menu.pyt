


nombre_list = []
codigo_list = []
telefono_list = []
puesto_list = []

contador_cod = 0



def listar_plantilla():
    for x in range(len(codigo_list)):
        print(f""" 
                Código: {codigo_list[x]}
                Nombre: {nombre_list[x]}
                Puesto: {puesto_list[x]}
                Teléfono: {telefono_list[x]}
            """)

def mostrar_persona(cod):
    for x in range(len(codigo_list)):
        if cod == codigo_list[x]:
            return f"""
                Código: {codigo_list[x]}
                Nombre: {nombre_list[x]} 
                Puesto: {puesto_list[x]}
                Teléfono: {telefono_list[x]}"""
        else:
            print("No se encontro el elemento")

def insertar_persona(nombre, telefono, puesto):
    global contador_cod 
    contador_cod += 1
    codigo_list.append(contador_cod)
    nombre_list.append(nombre)
    puesto_list.append(puesto)
    telefono_list.append(telefono)
    print(f"Se agrego satisfactoriamente")
    

def eliminar_persona(cod):
    for x in range(len(codigo_list)-1,-1,-1):
        if codigo_list[x] == cod:
            #print(codigo_list[x])
            #print(nombre_list[x])
            #print(puesto_list[x])
            #print(telefono_list[x])
            codigo_list.pop(x)
            nombre_list.pop(x)
            puesto_list.pop(x)
            telefono_list.pop(x)
            print("Eliminado satisfactoriamente")

def actualizar_persona(cod):
    try:
        for x in range(len(codigo_list)):
            if codigo_list[x] == cod:
                nombre_list[x] = input("Ingrese el nuevo nombre: ")
                puesto_list[x] = input("Ingrese el nuevo puesto: ")
                telefono_list[x] = int(input("Ingrese el nuevo número de telefono: "))
                print("Se actualizó correctamente")
    except Exception as e:
        print(e)
    

#listar_plantilla()
insertar_persona("Diego",312312312,"Ing Sistemas")
#listar_plantilla()
insertar_persona("Camilo",1312312,"Ing Civil")
#listar_plantilla()
insertar_persona("Eduvina",311231231,"Secretaria")
#listar_plantilla()

#eliminar_persona(1)
#listar_plantilla()
insertar_persona("Karen", 3123123123, "Graficadora")
insertar_persona("Natalia", 31231231,"Medicina")
#listar_plantilla()
#actualizar_persona(4)
listar_plantilla()
print(mostrar_persona(1))

#print(f""" 
#        Cod: {codigo_list} 
#        Nom: {nombre_list}
#        Puesto: {puesto_list}
#       Telefono: {telefono_list}""")

#print(codigo_list[0])


#contador = 10

#def reiniciar_contador():
#   global contador
#    contador = 0


# print(f'Contador antes es {contador}')
# reiniciar_contador()
# print(f'Contador después es {contador}')