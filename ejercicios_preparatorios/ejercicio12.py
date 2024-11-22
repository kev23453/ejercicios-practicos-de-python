'''

PROGRAMA QUE LEA LA EDAD DEL USUARIO. SI ES MAYOR QUE 50 MOSTRAR MENSAJE 
QUE DIGA "ABUELO." SI ES MAYOR QUE 30 MOSTRAR MENSAJE QUE DIGA "PADRE".
EN CASO CONTRARIO MOSTRAR MENSAJE QUE DIGA "HIJO"

'''
edad = int(input("ingresa la edad: "))

if edad > 50:
    print("Abuelo")
elif edad > 30:
    print("Padre")
else:
    print("hijo")