'''
6. Desarrolla un programa que calcule el Índice de Masa Corporal (IMC)
a partir del peso y la altura del usuario, e imprima su categoría de salud
basada en el IMC.

Clasifica el IMC de la siguiente forma:

Menos de 18.5: Bajo peso.
Entre 18.5 y 24.9: Peso normal.
Entre 25 y 29.9: Sobrepeso.
30 o más: Obesidad.


El índice de masa corporal (IMC) es el peso de una persona en kilogramos
dividido por el cuadrado de la estatura en metros.

'''

peso = float(input("ingresa el peso: "))
altura = float(input("ingresa la altura: "))

imc = peso / altura**2

if imc < 18.5 :
    print(f"tu peso es de: {imc} - bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print(f"tu peso es de: {imc} - peso normal")
elif imc >= 25 and imc <= 29.9:
    print(f"tu peso es de: {imc} - sobrepeso")
else:
    print(f"tu peso es de: {imc} - obesidad")





'''imc = peso / altura'''




