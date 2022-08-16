from machine import Pin
from utime import sleep
import _thread
#=========================Configuration===========================#
LedRed=Pin(0,Pin.OUT)
LedYellow=Pin(1,Pin.OUT)
LedGreen=Pin(2,Pin.OUT)
Button=Pin(3,Pin.IN,Pin.PULL_DOWN)
Buzzer=Pin(4,Pin.OUT)
Sensor=Pin(18,Pin.IN,Pin.PULL_DOWN)
#=============================Variable==================================#
global ButtonPressed
global SensorDetected
ButtonPressed=False
SensorDetected=False
#===========================thread Alarme===============================#
def Alarme():
    global ButtonPressed
    global SensorDetected
    while True:
        if Sensor.value()==1:
            SensorDetected=True
        if Button.value()==1:
            ButtonPressed=True
    sleep(0.1)
_thread.start_new_thread(Alarme,())
#===============================Main====================================#
while True:
    ButtonPressed = False
    LedGreen.value(1)
    LedRed.value(0)
    LedYellow.value(0)
    Buzzer.value(0)
    while SensorDetected==True:
        LedGreen.value(0)
        LedRed.toggle()
        LedYellow.toggle()
        sleep(0.05)
        Buzzer.toggle()
        if ButtonPressed==True:
             SensorDetected=False
        
