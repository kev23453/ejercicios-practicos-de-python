edad = int(input("ingresa la edad: "))

cuadrado_de_edad = edad ** 2
suma_edad = edad + 40
resta_edad = edad - 10
divide_edad = edad / 3
residuo = edad % 2


print(f"el cuadrado de la edad es {cuadrado_de_edad}")
print(f"{edad} + 40 es igual a {suma_edad}")
print(f"{edad} - 10 es igual a {resta_edad}")
print(f"{edad} / 3 es igual a {divide_edad}")

if residuo == 0:
    print(f"{edad} es par")
else:
    print(f"{edad} es impar")