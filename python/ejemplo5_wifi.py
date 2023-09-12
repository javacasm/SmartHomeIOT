# ejemplo 5 - wifi

# https://github.com/lionyhw/EF_Produce_MicroPython 

from IoTbit import IOT


def test_wifi():

    iot = IOT()
    if iot.connectWIFI("DIGIFIBRA-4BB8_plus","qazxcvbgtrewsdf26"):
        display.show(Image.YES)
    else:
        display.show(Image.NO)
  