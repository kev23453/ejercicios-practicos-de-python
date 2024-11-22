'''

Elabore un programa que cumpla con lo siguiente:

Solicitar al usuario su nombre, su edad, su mes de nacimiento y su peso 
corporal en libras.



Calcular los meses que ha vivido 

Si los meses que ha vivido son mas de 200, convertir su peso a kilogramos.
En caso contrario convertirlo a onzas.

Si el peso en kilogramos es menor que 50, y la edad en años es mas que 18,
mostrar mensaje "estas flaco/a".

Si el peso en kilogramos es menor que 50 y la edad en años es menor que 18,
mostrar mensaje "estas normal"

En caso contrario mostrar mensaje: "vuelve en un mes"



Utilizando la estructura match evalúe el mes de nacimiento y escriba el 
nombre del mes en que nació el usuario en INGLES, a modo de traducción.

'''

nombre = input("ingresa tu nombre: ")
edad = int(input("ingresa tu edad: "))
mes_nacimiento = int(input("ingresa tu mes de nacimiento: "))
peso_lb = float(input("ingresa tu peso en libras: "))

meses_año = 12

#meses que ha vivido
meses_vividos = meses_año * edad

if meses_vividos > 200:
    lb_to_kg = peso_lb * 0.453592
    
    if lb_to_kg < 50 and edad > 18:
        print("Estas flaco")
    elif lb_to_kg < 50 and edad < 18:
        print("Estas normal")
    else:
        print(f"vuelve en un mes tu peso es {lb_to_kg}")

else:
    lb_to_oz = peso_lb * 16
    print(f"tu peso en onzas es{lb_to_oz}")
    
    
    
match mes_nacimiento:
    case 1:
        print("January")
    case 2:
        print("Febraury")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")