from machine import Pin             #Biblioteca dos pinos
from machine import I2C             #Biblioteca do I2C
from lcd_api import LcdApi          #Biblioteca de configuração do display
from pico_i2c_lcd import I2cLcd     #Biblioteca de configuração do display
from machine import PWM             #Biblioteca do PWM
from utime import sleep             #Biblioteca do delay
import _thread                      #Biblioteca da thread
#=================================Display===========================#
Address = 0x27                      #Endereço I2C
Rows = 2                            #Número de linhas
Cols = 16                           #Número de colunas
i2cConfig=I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)   #Configurações do hardware I2C
lcd = I2cLcd(i2cConfig,Address,Rows, Cols)          #Configurações do display
#=================================Variable==========================#
global UpButton                      #Variável global para botão Up
global DownButton                    #Variável global para botão Down
UpButton = False                     #Up como Falso
DownButton=False                     #Down como Falso                   
PwmOut=PWM(Pin(28))                  #Pino do PWM
PwmOut.freq(1000)                    #Frequência
Up = Pin(3,Pin.IN,Pin.PULL_DOWN)     #Configura botão Up
Down = Pin(2,Pin.IN,Pin.PULL_DOWN)   #Configura botão Down
Value=50                             #Valor inicial do PWM
#===================================Thread==========================#
def Pressed ():                      #Thread   
    global UpButton                  #Chama as variáveis globais
    global DownButton                #Chama as variáveis globais
    while True:                      #Loop
        if Up.value()==1:            #Se botão Up pressionado...
             UpButton=True           #Variável vira Verdadeira
             sleep(0.2)              #delay 200mS
        if Down.value()==1:          #Se botão Down pressionado...
             DownButton=True         #Variável vira Verdadeira
             sleep(0.2)              #delay 200mS
_thread.start_new_thread(Pressed,()) #Inicia a thread
#===================================Main============================#
while True:                                     #Loop principal
    if UpButton==True and Value<95:             #Se botão Up pressionado e PWM menor que 95%...
        Value=Value+5                           #Incrementa o Value de 5 em 5
        global UpButton                         #Chama as variáveis globais
        UpButton=False                          #Define Up como falso
    if DownButton==True and Value>10 :          #Se botão Down pressionado e PWM maior que 10%...
        Value=Value-5                           #Decrementa o Value de 5 em 5
        global DownButton                       #Chama as variáveis globais
        DownButton=False                        #Define Down como falso
    ValuePwm=Value*650                          #Converter o valor do PWM para 16 bits
    PwmOut.duty_u16(ValuePwm)                   #Aplica o valor do Duty da saída PWM
    lcd.move_to(1,0)                            #Movimenta o cursor
    lcd.putstr("Motor Control")                 #Imprime na tela
    lcd.move_to(1,1)                            #Movimenta o cursor
    lcd.putstr("PWM in: "+str(Value)+" %")      #Imprime 'Value' no display