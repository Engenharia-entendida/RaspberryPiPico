from machine import Pin   
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime
#=================================Display==========================#
Address = 0x27  
Rows = 2
Cols = 16
i2cConfig=I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
lcd = I2cLcd(i2cConfig,Address,Rows, Cols)
#===================================Sensor==========================#
Trigger = Pin(3,Pin.OUT)
Echo = Pin(2,Pin.IN)
#===================================Main============================#
while True:
    Trigger.value(1)
    utime.sleep_us(10)
    Trigger.value(0)
    while Echo.value()==0:
        Off=utime.ticks_us()
    while Echo.value()==1:
        On=utime.ticks_us()
        distance=(On-Off)/58
    lcd.move_to(1,0)
    lcd.putstr("Digital Scale!")
    lcd.move_to(1,1)
    lcd.putstr("In CM: "+str(distance)+"")