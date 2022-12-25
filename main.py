import machine                                     #Biblioteca para utilização dos pinos do Raspberry.
import socket                                      #Biblioteca para utilização do socket.
import network                                     #Biblioteca para utilização das configurações de rede.
from time import sleep                             #Biblioteca para utilização do delay.
#============================================Configurações iniciais===================================================#
wlan = network.WLAN(network.STA_IF)                #Configura o Raspberry como um ponto que irá se conectar a rede.
wlan.active(True)                                  #Habilita o W-Fi.
wlan.connect("Dhanuzio 2.4Ghz","Error401")         #Configura o nome da rede e a senha.
led=machine.Pin('LED',machine.Pin.OUT)             #Configura o LED onboard da placa como saída.
#============================================Configurações iniciais===================================================#
while wlan.isconnected() == False:                 #Se não houver conexão...
    print('Waiting connection...')                 #Exibe mensagem.
    sleep(1)                                       #Espera 1 Segundo.                                          
if wlan.isconnected() == True:                     #Se houver conexão.
    print('connected')                             #Exibe mensagem.
    ip=wlan.ifconfig()[0]                          #Atribue o ip do Raspberry a variável.
    print('IP: ', ip)                              #Exibe o ip do Raspberry
#===================================================Página web========================================================# 
def webpage(value):
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <form action="./on">
            <input type="submit" value="Led On" />
            </form>
            <form action="./off">
            <input type="submit" value="Led Off" />
            </form>
            </body>
            </form>
            <p>Temperature is {value} degrees Celsius</p>
            </body>
            </html>
            """
    return html
#=========================================Verifica a conexão com o serve==============================================# 
def serve(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        print(request)
        
#===================================Verifica os dados que retornam da página===========================================#         
        if request == '/on?':                                                        #Se o dado recebido é "on".                      
            led.high()                                                               #Liga o led.
        elif request == '/off?':                                                     #Se o dado recebido é "off".  
            led.low()                                                                #Desliga o led.
        Sensor = machine.ADC(4)                                                      #Configura o sensor de temperatura onboard.
        conversion_factor = 3.3 / (65535)                                            #Fator de conversão
        value = 27 - ((Sensor.read_u16() * conversion_factor) - 0.706)/0.001721      #Cálculo para temperatura em  Celsius
        html=webpage(value)                                                          #Html recebe value
        client.send(html)                                                            #Envia o para a página
        client.close()                                                               #Encerra
#====================================================Inicia o socket===================================================# 
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)
#====================================================Tenta a conexão===================================================# 
try:
    if ip is not None:
        connection=open_socket(ip)
        serve(connection)
except KeyboardInterrupt:
    machine.reset()