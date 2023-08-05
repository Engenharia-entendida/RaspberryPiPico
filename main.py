from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import dht
WIDTH  = 128                                            
HEIGHT = 64                                            
sensor = dht.DHT22(Pin(19))
fan = Pin(16,Pin.OUT)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)       
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  
 
while True:
    oled.fill(0)
    sensor.measure()
    temp = (sensor.temperature())
    hum = (sensor.humidity())
    oled.text("Engenharia",24,0)
    oled.text("entendida",30,12)
    oled.text("Temperatura:",2,22)
    oled.text(str(temp) + "C",2,32)
    oled.text("Umidade",2,44)
    oled.text(str(hum) + "%",2,53)
    oled.show()
    if temp>45:
        fan.on()
    else:
        fan.off()
    sleep(1)