from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from machine import ADC
import _thread
sleep(1.5)
WIDTH = 128
HEIGHT = 64
Button = Pin(15, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
global Run
Run = True
SensorVolts1=ADC(26)
SensorCurrent=ADC(28)
Total = 0
Volts = 0
Amp = 0
#============================================================#
def voltimeter():
    oled.fill(0)
    oled.text("Voltimetro", 24, 0)
    oled.text("Volts: {:.3f}V".format(Volts), 2, 18)
    oled.show()
    sleep(0.1)
def amperimeter():
    oled.fill(0)
    oled.text("Amperimetro", 24, 0)
    oled.text("Current: {:.3f}A".format(Amp), 2, 18)
    oled.show()
    sleep(0.1)
def Alert():
    oled.fill(0)
    oled.text("Amperimetro", 24, 0)
    oled.text("Pontas Invertidas!", 2, 20)
    sleep(1)
    oled.show()
#=========================Thread=============================#
def Pressed():
    global Run
    while True:
        if Button.value()==0:
            Run = not Run
        sleep(0.003)
_thread.start_new_thread(Pressed,())
#============================Loop=============================#
while True:
    while (Run==True):
        Total=0
        for i in range(50):
            Volts1 = SensorVolts1.read_u16()
            Total += Volts1
            sleep(0.01)
        Total=Total/50
        Volts=Total*(3.3/65535)
        Volts=(Volts - 1.623) * 14.9981
        voltimeter()
    while (Run==False):
        Total=0
        for i in range(50):
            Amp1 = SensorCurrent.read_u16()
            Total += Amp1
            sleep(0.01)
        Total=Total/50
        Amp=Total*(3.3/65535)
        Amp=(Amp - 1.411) * 0.985
        if Amp < 0:
            Alert()
        else:
            amperimeter()