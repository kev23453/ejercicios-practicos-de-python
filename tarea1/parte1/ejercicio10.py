'''
10. Leer dos números enteros de dos dígitos y determinar a cuánto es igual
la suma de todos los dígitos.
'''

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

if (numero1 >= 10 and numero1 <= 99) and (numero2 >= 10 and numero2 <= 99):
    int_to_str1 = str(numero1)
    int_to_str2 = str(numero2)
    
    resultado = int(int_to_str1[0]) + int(int_to_str1[1]) + int(int_to_str2[0]) + int(int_to_str2[1])
    print(f"la suma de todos los digitos es igual a {resultado}")
    
else:
    print("ambos numeros deben ser de 2 digitos")




