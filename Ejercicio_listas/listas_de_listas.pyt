lista_main = []

id = [1,2,3,4,5]
nombre = ["Diego","Camilo","Blanca","Mario","Yobany"]
apellido = ["Sanchez","Buitrago","Escobar","Cifuentes","Rodriguez"]
edad = [18,24,45,55,89]
estado = ["Soltero", "Casado","Divorciada","Viudo","Soltero"]

lista_main.append(id)
lista_main.append(nombre)
lista_main.append(apellido)
lista_main.append(edad)
lista_main.append(estado)
print(lista_main)


print(len(lista_main))

for i in range(len(id)):
    print(f"""
    ID: {id[i]}
    Nombre: {nombre[i]}
    Apellido: {apellido[i]}
    Edad: {edad[i]}
    Estado: {estado[i]}
    """)


#for i in range(len(nombre)):
#    print(f"""
#    Nombre: {nombre[i]}
#    Apellido: {apellido[i]}
#    Edad: {edad[i]}
#    Estado: {estado[i]}
#   """)
