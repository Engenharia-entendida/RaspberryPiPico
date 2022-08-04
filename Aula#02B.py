from machine import Pin
from time import sleep

LedRed=Pin(2,Pin.OUT)
LedYellow=Pin(3,Pin.OUT)
LedGreen=Pin(4,Pin.OUT)
while(True):
    LedRed.value(1)
    LedYellow.value(0)
    LedGreen.value(0)
    sleep(3)
    
    LedRed.toggle()
    LedYellow.toggle()
    sleep(1)
    
    LedYellow.toggle()
    LedGreen.toggle()
    sleep(3)