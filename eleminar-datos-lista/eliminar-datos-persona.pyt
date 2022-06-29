opcion = None


codigo = list()
nombre = list()
puesto = []
telefono = []





while opcion != "0":
    
    print("""Menú Principal:
        1- Ver Plantilla
        2- Insertar Persona
        3- Eliminar Persona
        4- Modificar Persona
        0- Salir""")

    opcion = input("Ingrese la opcion a realizar: ")
    if opcion == "1":
        print("|     Codigo     |     Nombre    |     Puesto     |     Telefono     |")
        for x in range(len(codigo)):
            print(f"""      {codigo[x]}              {nombre[x]}        {puesto[x]}       {telefono[x]}     """)
        print("Plantilla leída correctamente")

    elif opcion == "2":
        codigo.append(input("Ingrese el # de documento de la persona: "))
        nombre.append(input("Ingrese el nombre de la persona: "))
        puesto.append(input("Ingrese el puesto que ocupa: "))
        telefono.append(int(input("Ingrese su número de telefono: ")))
        print("La persona fue agregada exitosamente")

    
    elif opcion == "3":
        cod = input("Ingrese el codigo que quiere eliminar: ")
        for x in range(len(codigo)-1,-1,-1):
            if codigo[x] == cod:
                codigo.pop(x)
                nombre.pop(x)
                puesto.pop(x)
                telefono.pop(x)
                print("Codigo eliminado satisfactoriamente")

    elif opcion == "4":
        cod = input("Ingrese el codigo que quiere modificar: ")
        for x in range(len(codigo)):
            if codigo[x] == cod:
                nombre[x] = input("Ingrese el nuevo nombre: ")
                puesto[x] = input("Ingrese el nuevo puesto: ")
                telefono[x] = int(input("Ingrese el nuevo número de telefono: "))
                print("Persona actualizada correctamente")
    
    else: 
        print("Por favor digita una opcion correcta") 
