from machine import Pin
from machine import ADC
from machine import PWM
from utime import sleep
#==============================Variable=======================================#
Potentiometer=ADC(27)
PwmOut=PWM(Pin(15))
PwmOut.freq(1000)
#================================Main=========================================#
while True:
    PwmOut.duty_u16(Potentiometer.read_u16())
    sleep(0.1)
    print(PwmOut)