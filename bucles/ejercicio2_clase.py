'''
2. Crear un programa que reciba el nombre y la edad de una persona. 

Si la edad de la persona es mayor que 18, mostrar un mensaje que diga 
"Estudia en ITLA", la misma cantidad de veces que la edad. En caso contrario,
mostrar el mensaje solo 5 veces.
'''

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
mensaje = "Estudia en el ITLA"

'''WHILE'''
'''contador = 0

if edad > 18:
    while contador < edad:
        print(mensaje)
        contador += 1
else:
    while contador < 5:
        print(mensaje)
        contador += 1
        

    
print("-----------------------------------------")    
    
    

FOR'''    

'''for n in range(edad):
    print(f"hola {nombre}")    


print("-----------------------------------------")    
'''


'''simulacion de un Do while'''

contador = 0

while True: 
    print(f"estudias en el itla {nombre}")
    contador += 1
    
    if edad >= 18:
        if contador == edad:
            break;
    else:
        f = 5;
        if contador == f:
            break;