from machine import Pin   
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
#=================================Variable==========================#
Address = 0x27  
Rows = 2
Cols = 16
i2cConfig=I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
lcd = I2cLcd(i2cConfig,Address,Rows, Cols)
#===================================Main============================#
lcd.move_to(2,0)
lcd.putstr("Hello World!")
lcd.move_to(1,1)
lcd.putstr("Eng. entendida")