from machine import Pin, I2C, PWM,ADC
from ssd1306 import SSD1306_I2C
import utime
 
sensor = machine.ADC(27)
PwmOut=PWM(Pin(16))
PwmOut.freq(50)
WIDTH  = 128                                            
HEIGHT = 64                                            
 
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)       
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  
 
while True:
    PotValue=sensor.read_u16()
    angulo=int((PotValue - 0) * (7864.2 - 1638.37) / (65535 - 0) + 1638.27)
    PwmOut.duty_u16(angulo)
    reading = sensor.read_u16() /364
    oled.fill(0)
    oled.text("Engenharia",24,2)
    oled.text("entendida",30,14)
    oled.text("Servo Position:",2,30)
    oled.text(str(round(reading)),2,44)
    oled.text("Graus ",30,44)
    oled.show()
