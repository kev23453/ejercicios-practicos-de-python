'''
1. Programa que pida el nombre y la edad del usuario, y que muestre un saludo 
con el nombre del usuario, la cantidad de veces de la edad. 
(Ejemplo: si el nombre es "Luis" y la edad es 24,
debe mostrar el saludo: "Hola Luis" 24 veces)
'''

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))


'''WHILE'''

x = 0
while x < edad:
    print(f"Hola {nombre}")
    x+=1
    
print("------------------------------------")    
    
    

'''FOR'''    

for n in range(edad):
    print(f"hola {nombre}")    


print("------------------------------------")    



'''simulacion de un Do while'''

contador = 0

while True: 
    print(f"hola {nombre}")
    contador += 1
    
    if contador == edad:
        break    
    