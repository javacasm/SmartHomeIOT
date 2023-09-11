# Ejemplo 3 - neopixel

from microbit import *
import neopixel

np = neopixel.NeoPixel(pin16,1)

while True:
    np[0] = (0,255,0)
    np.show()
    sleep(500)
    np[0] = (255,0,0)
    np.show()
    sleep(500)
    np[0] = (0,0,255)
    np.show()
    sleep(500)
    for i in range(0,150,5):
        np[0] = (i,0,0)
        np.show()
        sleep(50)
    for i in range(150,0,-5):
        np[0] = (0,i,0)
        np.show()
        sleep(50)
