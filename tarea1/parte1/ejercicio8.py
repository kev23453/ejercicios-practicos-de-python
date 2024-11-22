'''
8. Leer dos números enteros de dos dígitos y determinar si tienen
dígitos comunes.

NO TERMINADO CORRECTAMENTE

'''

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

if (numero1 >= 10 and numero1 <= 99) and (numero2 >= 10 and numero2 <= 99):
    int_to_srt1 = str(numero1)
    int_to_srt2 = str(numero2)
    
    digito1_num1 = int(int_to_srt1[0])
    digito2_num1 = int(int_to_srt1[1])
    digito1_num2 = int(int_to_srt2[0])
    digito2_num2 = int(int_to_srt2[1])

    if (digito1_num1 == digito1_num2) or (digito1_num1 == digito2_num2):
        print(f"el primer digito coincide con uno de los digitos del segundo numero")
    elif (digito2_num1 == digito1_num1) or (digito2_num1 == digito1_num2):
        print("el segundo digito del primer numero coincide con uno de los del segundo numero") 
    else:
        print("ningun digito coincide entre si")
    
    
else:
    print("ambos numeros deben ser de 2 digitos >:) ")
    

