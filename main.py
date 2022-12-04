import network                                          #Importa biblioteca para rede Wi-Fi.
from utime import sleep                                 #Importa a biblioteca para uso de delay.
from machine import Pin                                 #Importa a biblioteca para usar o pinos do Raspberry.
#=============================================================================================================#
ssid = "Dhanuzio 2.4Ghz"                                #Nome da rede Wi-Fi.
password = "Error"                                      #Senha da rede Wi-Fi.
led=Pin("LED",Pin.OUT)                                  #Configura o led onboard como saída
z=0
#======================================Function to connect Wi-Fi==============================================#
while True:                                             #Loop principal.
    wlan = network.WLAN(network.STA_IF)                 #Configura o raspberry como ponto a ser conectado a rede.
    wlan.active(True)                                   #Inicia o Wi-Fi do Raspberry.
    wlan.connect(ssid,password)                         #Passa o nome da rede e senha para o Raspberry.
    while wlan.isconnected() == False and z<10:                  #Enquanto não houver conexão...
        print('Waiting for connection...')              #Exibe a mensagem.              
        sleep(1)                                        #Espera 1 segundo.
        z=z+1
    print('Erro na conexão.')
    while wlan.isconnected() == True:                   #Se a conexão for bem sucedida...
        print(wlan.ifconfig())                          #Exibe as configurações da rede.
        led.toggle()                                    #Muda o estado do led onboard.
        sleep(1)                                        #Delay de 1 segundo.
