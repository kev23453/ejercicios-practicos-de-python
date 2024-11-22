'''
Elabora un programa que cumpla con lo siguiente.

Debe contener una función llamada main() que le pida al usuario su nombre y su
edad. Esta función debe pasarle como parámetro la edad a otra función llamada 
verificacion(). Si el retorno de la función verificacion() es true, mostrar un 
mensaje que diga "Bienvenido", en caso contrario mostrar un mensaje que diga 
"Vuelva después"

La lógica de la función verificacion() es que debe validar si la edad es un 
número par y es mayor de edad, debe devolver true, en caso contrario devolver 
false.


A continuación debe llamar a una función llamada operaciones(). En esta función se
le van a solicitar al usuario dos números y luego se le va a presentar las opciones
básicas de una calculadora (sumar, restar, multiplicar dividir). 


Utilice la estructura match para que segun la opción que seleccione
el usuario llame a la función correspondiente, le pase los dos números y cuando
retorne el resultado, sea mostrado desde la función operaciones()



Por ejemplo, si el usuario ingresa los números 8,5 y elige la opcion restar,
debe llamar a una función con ese nombre, para que haga la resta de los dos 
números y retorne el resultado.
'''

def main():
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    
    return edad

def verificacion(edad):
    if edad % 2 == 0 and edad > 18:
        return "bienvenido"
    else:
        return "vuelva despues"
    
print(verificacion(main()))


print("*******************************************\n")



def sumar(a, b):
    return a+b

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(x, y):
    return x/y


def operaciones():
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    
    print("[1] - sumar")
    print("[2] - restar")
    print("[3] - multiplicar")
    print("[4] - dividir")
    
    operacion = int(input("que operacion deseas realizar? "))
    
    
    match(operacion):
        case 1:
            print(sumar(num1, num2))
        case 2:
            print(restar(num1, num2))
        case 3:
            print(multiplicar(num1, num2))
        case 4:
            print(dividir(num1, num2))
        case defecto:
            print("numero invalido")


operaciones()