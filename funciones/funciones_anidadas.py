def main():
    pedirValores()
    
def sumar(x, y):
    return x+y

def saludar(nombre):
    print(f"hola {nombre}")

def pedirValores():
    n1 = int(input("ingresar el 1er numero: "))
    n2 = int(input("ingresar el 2do numero: "))
    print(sumar(n1,n2))
    nom = input("ingrese su nombre: ")
    saludar(nom)
    
    
#solo hay que llamar a main

main()


#el return solamente devuelve un valor sin imprimirlo.


'''
para heredar de una clase en python no es necesario usar extends
si no de la siguiente manera

class clase_principal (nombre_de_la_otra_clase):
'''


