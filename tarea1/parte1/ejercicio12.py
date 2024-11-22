

numero = int(input("ingrese el numero: "))

if numero >= 100 and numero <= 999:
    strnum = str(numero)
    
    digit1 = int(strnum[0])
    digit2 = int(strnum[1])
    digit3 = int(strnum[2])
    
    if ( digit1 == digit2 or digit1 == digit3 or digit2 == digit3):
        print("hay numeros iguales")
    else:
        print("ningun numero coincide")
    
else:
    print("numero invalido")