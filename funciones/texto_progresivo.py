import time as tm

def mostrarTexto(texto, delay):
    for letra in texto:
        print(letra, end='', flush=True)
        tm.sleep(delay)
    print()
    
texto = "braily es un mmgvazo"
mostrarTexto(texto, 0.1)