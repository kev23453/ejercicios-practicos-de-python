'''
4.  Desarrolla un programa que solicite la edad de una persona
y clasifique en qué grupo etario se encuentra.

Si la persona tiene entre 0 y 12 años, muestra "Eres un niño."
Si tiene entre 13 y 17 años, muestra "Eres un adolescente."
Si tiene entre 18 y 64 años, muestra "Eres un adulto."
Si tiene 65 años o más, muestra "Eres un adulto mayor."
'''

edad = int(input("ingresa la edad que tienes: "))

if edad == 0 and edad == 12:
    print("Eres un niño")
elif edad == 13 and edad == 17:
    print("Eres un adolescente")
elif edad == 18 and edad == 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

