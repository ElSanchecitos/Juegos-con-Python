# En este juego vamos a concatenar cadenas de caracteres
# La cadena es: Aprende a programar con_________________. 

# organizacion = "freeCodeCamp"

# #Tipos de concatenacion en python
# print("Aprende a programar con " + organizacion)
# print(f"Aprende a programar con {organizacion}")
# print("Aprende a programar con {}".format(organizacion))
# print("Aprende a programar con", organizacion)

#Mad libs (Historias locas)

mad_lib = f"¡Programar es tan (1)__________! Siempre me emociona porque me encanta (2)_________problemas. ¡Aprende a (3)___________ con freeCodeCamp y alcanza tus metas (4)___________!"
print(mad_lib)

adj = input("1.Adjetivo: ")
contador = 0
while adj != "divertido":
    if contador == 0:
        print("La palabra es incorrecta intentelo de nuevo")
    elif contador==1:
        print("La palabra es incorrecta")
        print("Segundo intento")
    elif contador ==2:
        print("La palabra es incorrecta")
        print("Tercer intento")
    elif contador == 3: 
        adj = None
        break  
    contador+=1
    adj = input("1.Adjetivo: ")
    
    
        
verbo1 = input("2.verbo: ")
verbo2 = input("3.Verbo: ")
sustantivo_plural = input("4.Sustantivo (plural): ")

mad_lib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus metas {sustantivo_plural} !"

print(mad_lib)
