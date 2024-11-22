'''
Desarrolla un programa que reciba una letra de calificación (A, B, C,F)
y devuelva una descripción correspondiente: Si fue A, que muestre en consola
"Excelente". Si fue B, que muestre en consola "Bueno", si fue C, que muestre
en consola "Deficiente" y si fue F que muestre "Reprobado" Utiliza una 
estructura switch para este propósito.
'''

calificacion = input("ingresa una letra de calificacion: ") 

match calificacion:
    case "a":
        print(f"Excelente")
    case "b":
        print(f"Bueno")
    case "c":
        print(f"Deficiente")
    case "f":
        print(f"reprobado")
    case defecto:
        print(f"la letra no es valida")