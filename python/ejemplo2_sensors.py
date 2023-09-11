# Ejemplo 2 - sensores analógicos

from microbit import *

# valores entre 0 y 1023

# Lectura del sensor de luz en p1 y 
# de temperatura TMP36 en P2

while True:
    analog_p2 = pin2.read_analog()
    temp = (analog_p2 * 3.3 /1023 - 0.5) * 100
    # degreesC = (voltage - 0.5) * 100.0 https://learn.sparkfun.com/tutorials/tinker-kit-circuit-guide/circuit-9-temperature-sensor
    print(pin1.read_analog(), analog_p2, temp, temperature())
    sleep(200)
    