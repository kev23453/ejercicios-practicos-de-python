#1.  Programa 1

#Desarrolla un programa en Python que calcule el puntaje final de un cuestionario basado en el número de respuestas correctas, incorrectas y no contestadas.

#Requerimientos:

#Solicita al usuario su nombre.
#Pide que ingrese:
# el número total de preguntas que tiene el examen
#el número de respuestas correctas
#el número de respuestas incorrectas.
#el número de preguntas no contestadas (dejadas vacías).
#Calcula el puntaje total y muestra el nombre del usuario con su puntaje alcanzado.
#Nota: La puntuación total es en base a 100 pts.

nombre = input("ingrese su nombre: ")
cantidad_preguntas = int(input("ingrese la cantidad de preguntas de su examen: "))
respuestas_correctas = int(input("ingrese el numero de preguntas correctas: "))
respuestas_incorrectas = int(input("ingrese el numero de preguntas incorrectas: "))
respuestas_vacias = int(input("ingrese las respuestas que tiene vacia: "))
total_puntaje = 100

respuestas_correctas = (respuestas_correctas / cantidad_preguntas) * total_puntaje 
respuestas_incorrectas = (respuestas_incorrectas / cantidad_preguntas) * total_puntaje
respuestas_vacias = (respuestas_vacias / cantidad_preguntas) * total_puntaje


calculo = total_puntaje - respuestas_incorrectas - respuestas_vacias

print(f"{nombre} su nota final del examen es {calculo}")


print(f"respuestas correctas: {respuestas_correctas}")
print(f"respuestas incorrectas: {respuestas_incorrectas}")
print(f"respuestas vacias: {respuestas_vacias}")




