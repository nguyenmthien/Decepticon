import time
import binascii as bi
import socket

def connecting(ip, port):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

def send_message(message):
    s.send(message)

if __name__ == '__main__':
    connecting('192.168.137.128', 23)

    while True:
        number = input()
        string = str(number)
        message = bytes(string, 'utf-8')
        send_message(message)