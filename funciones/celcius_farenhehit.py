'''
declara una funcion que convierta los grados de celcius a Fahrenheit
y a la inversa dependiendo si el usuario coloca la opcion que quiere.
'''

print("Conversor de Temperaturas")
print("ingresa [1] para C° a F° [2] para F° a C° ")

# (4 °C × 9/5) + 32 = 39.2 °F  celcius a farenhehit
# (32 °F − 32) × 5/9 = 0 °C   farenhehit a celcius

def converTemperatures (numero, grados):   
    if(numero != 1 and numero != 2):
        print(f"la operacion que deseas hacer no existe, ingresa un numero valido")
    else:
        if(numero == 1):
            formula = round((grados * 9/5) + 32, 2)
            print(f"{grados}° celcius son {formula}° en farenhehit")
        else:
            formula = round((grados - 32) * 5/9, 2)
            print(f"{grados}° farenhehit son {formula}° en celcius")
            
            
preguntar = int(input("que operacion deseas realizar? "))
grado = int(input("ingresa el numero de grados: "))


converTemperatures(preguntar, grado)


