from machine import Pin
from utime import sleep
import _thread
#===========================Configuration================================#
LedRed=Pin(0,Pin.OUT)
LedYellow=Pin(1,Pin.OUT)
LedGreen=Pin(2,Pin.OUT)
Button=Pin(3,Pin.IN,Pin.PULL_DOWN)
Buzzer=Pin(4,Pin.OUT)
#===============================Variable=================================#
global ButtonPressed
ButtonPressed=False
#================================thread==================================#
def Pressed():
    global ButtonPressed
    while True:
        if Button.value()==1:
            ButtonPressed=True
        sleep(0.1)
_thread.start_new_thread(Pressed,())
#=================================Main===================================#
while True:
    LedYellow.value(0)
    LedRed.value(1)
    if ButtonPressed==True:
        for i in range(10):
            Buzzer.value(1)
            sleep(0.25)
            Buzzer.value(0)
            sleep(0.25)
        global ButtonPressed
        ButtonPressed = False
    else:
        sleep(5)
    LedRed.value(0)
    LedGreen.value(1)
    sleep(5)
    LedGreen.value(0)
    LedYellow.value(1)
    sleep(2)