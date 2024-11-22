'''
PROGRAMA QUE LEA UN NUMERO DE DOS DÍGITOS Y DETERMINE SI AMBOS DÍGITOS
SON PARES O IMPARES. DEBE MOSTRAR UN MENSAJE DANDO LA INFORMACIÓN DE CADA
DÍGITO (DECIR: "EL 1ER DÍGITO ES __(PAR  O IMPAR), EL SEGUNDO...").
'''

#numero % 2 == 0


numero = input("ingresa el numero entre 10 y 99: ")

primer_valor = int(numero[0])
segundo_valor = int(numero[1])

if primer_valor % 2 == 0:
    print(f"el {primer_valor} es par")
else:
    print(f"el {primer_valor} es impar")


if segundo_valor % 2 == 0:
    print(f"el {segundo_valor} es par")
else:
    print(f"el {segundo_valor} es impar")





