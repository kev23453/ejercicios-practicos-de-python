'''
Hacendo uso de match, realice lo siguiente:

Programa que le pida al usuario una letra de las siguientes: C, R, T, D, H

Si el usuario inserta una C, mostrar mensaje diciendo que es un circulo
Si el usuario inserta una R, mostrar mensaje diciendo que es un rectángulo
Si el usuario inserta una T, mensaje diciendo que es un triángulo 
Si el usuario inserta una D, mensaje diciendo que es un cuadrado.
Si el usuario inserta una H, mensaje diciendo que es un hexágono.
Si el usuario inserta una letra diferente a estas, mostrar un mensaje 
personalizado indicando el error.


'''

mensaje = "coloca una de las siguientes letras y te diremos a que figura corresponde"
letras = " C , R , T , D , H: "

letra = input(mensaje+letras)

match letra:
    case "C":
        print(f"C corresponde a un circulo")
    case "R":
        print(f"R corresponde a un rectangulo")
    case "T":
        print(f"T corresponde a un triangulo")
    case "D":
        print(f"D corresponde a un cuadrado")
    case "H":
        print(f"H corresponde a un hexagono")
    case defecto:
        print("la letra que haz colocado no es valida, inserta una de las que se te indica")

        