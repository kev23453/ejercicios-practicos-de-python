'''
Crea un programa que tome un número (del 1 al 7) e imprima el
día de la semana correspondiente
(por ejemplo, 1 para "Lunes", 2 para "Martes", etc.). 
Utiliza una estructura switch para determinar el día.
'''

numero = int(input("ingresa un numero del 1 al 7: "))

match numero:
    case 1:
        print(f"{numero}: es lunes")
    case 2:
        print(f"{numero}: es martes") 
    case 3:
        print(f"{numero}: es miercoles")
    case 4:
        print(f"{numero}: es jueves")
    case 5:
        print(f"{numero}: es viernes")
    case 6:
        print(f"{numero}: es sabado")
    case 7:
        print(f"{numero}: es domingo")
    case defecto:
        print(f"{numero} numero no valido")       
