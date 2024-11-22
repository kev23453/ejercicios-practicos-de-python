'''
Leer un número entero y determinar si es un número terminado en 4.'''

'''arreglo = []
numero = int(input("ingrese un numero entero: "))

for di in str(numero):
    arreglo.append(di)
    
ultimo_digito = arreglo[-1]
if(ultimo_digito == '4'):
    print(f"el numero {numero} termina en 4")
else:
    print(f"el numero {numero} ingresado no termina en 4")'''
#----------------------------------------------------------------------
    
    
numero = int(input("Ingrese un número entero: "))

# Obtener el último dígito usando la operación módulo
ultimo_digito = numero % 10

if ultimo_digito == 4:
    print(f"El número {numero} termina en 4")
else:
    print(f"El número {numero} no termina en 4")

