# Ejemplo 1 - smileys

# Importamos todo lo que necesitamos
from microbit import *


# Codigo en el bucle 'while True:' repite para siempre
while True:
    display.show(Image.SAD)
    sleep(1000)
    display.show(Image('00000:'
                       '09090:'
                       '00000:'
                       '55555:'
                       '00000'))
    sleep(500)
    display.show(Image.HAPPY)
    sleep(500)