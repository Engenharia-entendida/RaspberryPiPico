from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from machine import ADC
sleep(1.5)
WIDTH = 128
HEIGHT = 64
Button = Pin(15, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
Run = True
SensorVolts2=ADC(27)
SensorVolts1=ADC(26)
def voltimeter():
    oled.fill(0)
    oled.text("Voltimetro", 24, 0)
    oled.text("Volts: {:.3f}V".format(Volts), 2, 18)
    oled.show()
    sleep(0.01)
def amperimeter():
    oled.fill(0)
    oled.text("Amperimetro", 24, 0)
    oled.show()
    sleep(0.01)
while True:
    Total=0
    for i in range(150):
        Volts1 = SensorVolts1.read_u16()
        Total += Volts1
        sleep(0.012)
    Total=Total/150
    Volts=Total*(3.28/65535)
    Volts=(Volts - 1.64) * 14.16
    ButtonState = Button.value()
    if ButtonState == 0:
        Run = not Run
        sleep(0.1)
    if Run:
        voltimeter()
    else:
        amperimeter()
