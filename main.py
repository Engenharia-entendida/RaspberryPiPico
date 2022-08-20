from machine import ADC
from utime import sleep
#==============================================================#
Sensor=ADC(4)
while True:
    Read=(Sensor.read_u16()*3.3)/65535
    Temperature = 27 - (Read - 0.706)/0.001721
    print(Temperature)
    sleep(1)