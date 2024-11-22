'''
Crea un programa que tome un número (del 1 al 12) e
imprima el nombre del mes correspondiente (por ejemplo,
1 para "Enero", 2 para "Febrero", etc.). 
Utiliza una estructura switch para determinar el mes

'''

mes = int(input("ingrese un numero del 1 al 12 y diremos el mes correspondiente: "))

match mes:
    case 1:
        print(f"{mes} corresponde a Enero");
    case 2:
        print(f"{mes} corresponde a Febrero");
    case 3:
        print(f"{mes} corresponde a Marzo");
    case 4:
        print(f"{mes} corresponde a Abril");  
    case 5:
        print(f"{mes} corresponde a Mayo");  
    case 6:
        print(f"{mes} corresponde a Junio");  
    case 7:
        print(f"{mes} corresponde a Julio");  
    case 8:
        print(f"{mes} corresponde a Agosto");  
    case 9:
        print(f"{mes} corresponde a Septiembre");  
    case 10:
        print(f"{mes} corresponde a Octubre");  
    case 11:
        print(f"{mes} corresponde a Noviembre");  
    case 12:
        print(f"{mes} corresponde a Diciembre");  
    case defecto:
        print("el numero que colocaste no es valido")