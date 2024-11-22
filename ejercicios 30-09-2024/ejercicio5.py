'''
5. 

Crea un programa que solicite la calificación numérica de un examen
(del 0 al 100) e imprima la letra correspondiente según la siguiente escala:

90-100: A  | 80-89: B  |  70-79: C  |   60-69: D |   0-59: F

'''
calificacion = int(input("ingresa tu calificacion: "))

if calificacion > 90 and calificacion < 100:
    print("A")
elif calificacion > 80 and calificacion < 89:
    print("B")
elif calificacion > 70 and calificacion < 79:
    print("C")
elif calificacion > 60 and calificacion < 69:
    print("D")
elif calificacion > 0 and calificacion <  59:
    print("F")
else:
    print("el rango de valores es entre 0 y 100")
