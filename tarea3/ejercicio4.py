'''
4. Construir una función que reciba dos parámetros: el nombre y el apellido de 
una persona. Debe retornar el nombre complete
'''

def nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

def main():
    nombre = input("ingresa el nombre: ")
    apellido = input("ingresa el apellido: ")
    
    print(nombre_completo(nombre, apellido))
    
main()