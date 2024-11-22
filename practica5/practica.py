'''

Realice un programa que cumpla con lo siguiente:

Función main

Solicitarle al usuario su edad.
A continuación, solicitarle al usuario que ingrese 5 números y los almacene
en un arreglo. A continuación pasarle ese arreglo como parámetro a una función 
llamada cálculos. 



Lógica de la función calculos

Debe recibir un arreglo de 5 valores y multiplicar cada elemento del arreglo
por la edad del usuario e ir ingresando cada valor calculado en un nuevo arreglo. 
Ahí mismo debe pasarle el nuevo arreglo a otra función llamada total.
Cuando reciba el resultado de la función total, debe pasárselo a otra función 
llamada verificacion. La funcion verificacion harás las acciones finales del
programa.



Lógica de la función total:

La funcion total debe recibir un arreglo de 5 números y calcular la sumatoria de
los valores que sean mayor o igual que 100 y devolver / retornar ese valor a la
funcion calculos.



Lógica de la función verificación:

Esta función debe recibir un valor y evaluar si este valor es mayor o igual que 
500. Si es así, mostrar el mensaje "Valor alcanzado" el número de veces de la 
edad del usuario, en caso contrario, mostrar el mensaje "valor insuficiente" solo
una vez.


'''




def main():
    arreglo = []
    edad = int(input("ingrese su edad: "))
    for x in range(0, 5):
        numero = int(input("ingrese un numero: "))
        arreglo.append(numero)    
    
    calculos(arreglo,edad)
    

nuevo_arreglo = []
def calculos(arreglo_c,edad):
    for x in arreglo_c:
        multiplo = x*edad
        nuevo_arreglo.append(multiplo)
    total(nuevo_arreglo, edad)

        
        
def total(arreglo, edad):
    acumulador = 0
    for x in arreglo:
        if int(x) >= 100:
            acumulador += x
            acumulador = int(acumulador)
            
    verificacion(acumulador, edad)



def verificacion(total, edad):
    if total >= 500:
        for x in range(1, edad+1):
            print(f"{x} - {total} valor alcanzado")
    else:
        print(f"{x} - {total} valor insuficiente")
        

main()