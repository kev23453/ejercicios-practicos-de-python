#2. Programa 2

# Desarrolla un programa en Python que le pida al usuario su nombre y su edad.
# A continuación, el programa debe mostrarle al usuario:

#El numero de meses que ha vivido #El numero de semanas que ha vivido
#El numero de dias que ha vivido #El numero de horas que ha vivido
#El numero de minutos que ha vivido #El numero de segundos que ha vivido 

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

meses_año = 12
semanas_año = 52
dias_año = 365
horas_año = 8760
minutos_año = 525600
segundos_año = 31536000
#cuantos meses tiene un año

meses = edad * meses_año
semanas = edad * semanas_año
dias = edad * dias_año
horas = edad * horas_año
minutos = edad * minutos_año
segundos = edad * segundos_año

print(f"usted ha vivido {meses} meses, {semanas} semanas, {dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")

