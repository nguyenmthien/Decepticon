 #!/usr/bin/env python
import time
import binascii as bi
import socket

def connect (ip, port):
    TCP_IP=ip
    TCP_PORT=port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    
    
def sendMessage(message):
    message=MESSAGE
    MESSAGE=bytes("90",'utf-8')
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)    


if __name__=='__main__':
    connect('192.168.137.128',23)
    while True:
        previous_message = '1654984561'
        if (previous_message!=MESSAGE):
            sendMessage(MESSAGE)
        
    
        
        
        
