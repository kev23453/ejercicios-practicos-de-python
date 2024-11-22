import pygame
import time

# Inicializa Pygame
pygame.mixer.init()
pyg = pygame.mixer

# Carga el archivo de audio
pyg.music.load("resources/aud/8bit.mp3")
pyg.music.play()

# Mantiene el programa en ejecución mientras se reproduce la música
""" while pyg.music.get_busy():  # Espera hasta que termine la reproducción
    time.sleep(1)  # Pausa el programa brevemente
 """


quitd = input("deseas detener la musica (y/n): ")
if(quitd == "y"):
    pyg.music.stop()
elif(quitd == "n"):
    
else:
    print("no valido")

# Opción para detener la música
# pygame.mixer.music.stop()
