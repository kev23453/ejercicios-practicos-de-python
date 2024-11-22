def calcularISR(nombre, salario):
    salarios = [34685.00, 52027.42, 72260.25]
    taxes = [0.15, 0.20, 0.25]

    isr = 0
    
    if salario <= salarios[0]:
        print(f"{nombre} esta exedente de ISR (impuesto sobre la renta)")
    
    elif salario > salarios[0] and salario <= salarios[1]:
        isr = taxes[0] * (salario - salarios[0])
        print(f"{nombre} el impuesto sobre la renta que debe pagar es de: {isr}") 

    elif salario > salarios[1] and salario <= salarios[2]:
        isr = 2601.42 + taxes[1] * (salario - salarios[1])  
        print(f"{nombre} el impuesto sobre la renta que debe pagar es de: {isr}")
    
    else:
        #impuesto_fijo = 6648.49
        isr = 6648.49 + taxes[2] * (salario - salarios[2])
        print(f"el impuesto sobre la renta que debe pagar es de: {isr}")




nombre = input("ingrese su nombre: ")
sueldo = float(input("ingrese su salario: "))

calcularISR(nombre, sueldo)
