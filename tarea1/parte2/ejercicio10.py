'''
Ejercicio 10

Crea un programa que solicite una nota numérica entre 0 y 100. El programa debe 
clasificar la nota de acuerdo con las siguientes reglas:

Si la nota está entre 90 y 100, imprimir "Excelente".
Si está entre 70 y 89, imprimir "Aprobado".
Si está entre 50 y 69, imprimir "Suficiente".
Si es menor de 50, imprimir "Insuficiente".
 
'''

nota = int(input("ingrese su calificacion: "))

if(nota >= 0 and nota <= 100):
    if(nota >= 90 and nota <= 100):
        print("Excelente")
    elif(nota >= 70 and nota <= 89):
        print("Aprobado")
    elif(nota >= 50 and nota <= 69):
        print("Suficiente")
    else:
        print("insuficiente")
else:
    print("calificacion invalida")