import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from machine import ADC
sleep(1.5)
WIDTH = 128
HEIGHT = 64
Carga=Pin(2, Pin.OUT)
Descarga=ADC(28)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
Capacitancia = 0

#============================================================#
def printOled():
    oled.fill(0)
    oled.text("Capacitance", 24, 0)
    oled.text("C: {:.3f}Farads".format(Capacitancia), 2, 18)
    oled.show()
    sleep(0.1)
#============================Loop=============================#
while True:
    Carga.value(0)
    sleep(1)
    Carga.value(1)
    while (Descarga.read_u16()<40000):
        Tempo=utime.ticks_us()
    TempoCarga = utime.ticks_diff(utime.ticks_us(),Tempo)
    Capacitancia=TempoCarga/(1000*0.693)
    printOled()