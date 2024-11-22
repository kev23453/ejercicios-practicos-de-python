import time
from colorama import Style, init, Fore

init(autoreset=True)

def texto(texto, color, delay=0.16):
    match(color):
        case "red":
            color = Fore.RED
        case "yellow":
            color = Fore.YELLOW
        case "green":
            color = Fore.GREEN
        case "blue":
            color = Fore.BLUE
        case "white":
            color = Fore.WHITE
            
    for letra in texto:
        print(color + letra, end='', flush=True)
        time.sleep(delay)
    print()


        