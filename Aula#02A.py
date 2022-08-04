from machine import Pin
from utime import sleep

Led=Pin(2,Pin.OUT)
Button=Pin(5,Pin.IN,Pin.PULL_DOWN)
#=================================
while(True):
    if button.value()==1:
        Led.toggle()
    sleep(0.1)