import socket

from constants import *

SERVER = '192.168.0.9'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght)) # msg needs to have 64 bytes lenght (HEADER)
    client.send(send_lenght)
    client.send(message)

    # gotta improve this using the same threatment that receives messages o the server side
    print(client.recv(2048).decode(FORMAT))

# --------------------------------------------------------------------------------------------
# tests
input()
send_msg("Hello World")
input()
send_msg("Hello everyone")
input()
send_msg(DISCONNECT_MESSAGE)