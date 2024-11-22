def saludar(nombre):
    print(f"hola {nombre}")

nombrei = input("ingrese un nombre: ")
saludar(nombrei)




def saludarParam(nombre):
    return nombre;

nombre = input("ingrese su nombre: ")
print(f"{saludarParam(nombre)}")




def cuadrado(x):
    return x**2

numCuadrado = int(input("ingrese un numero: "))
print(cuadrado(numCuadrado))





def cubo(x):
    return x**3

numCubo = int(input("ingrese un numero: "))
print(cubo(numCubo))