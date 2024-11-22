def potencia(base, exponente):
    resultado = base**exponente
    return resultado


base = int(input("ingresa la base: "))
exponent = int(input("ingresa el exponente: "))

print(potencia(base, exponent))