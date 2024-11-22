edad = int(input("ingresa la edad: "))

es_mayor = (edad >= 18) * "es mayor"
es_menor = (edad < 18) * "es menor"

resultado = es_mayor + es_menor
print(resultado)

