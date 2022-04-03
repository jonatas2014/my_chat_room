import socket

from constants import *

SERVER = '192.168.0.9'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):

    '''Receives a message as a string do the necessary transformations
       to send to the server'''
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght)) # msg needs to have 64 bytes lenght (HEADER)
    client.send(send_lenght)
    client.send(message)

    # gotta improve this using the same threatment that receives messages o the server side
    # (future plans: wait for proper ui)
    #print(client.recv(2048).decode(FORMAT))

# --------------------------------------------------------------------------------------------
# tests
'''input()
send_msg("Hello World")
input()
send_msg("Hello everyone")
input()
send_msg(DISCONNECT_MESSAGE)'''

# ------------------------------------------------------------------------------------------------

def client_loop():

    '''Main client program'''

    # user digits his username
    print("please!!! pickup a username: ", end='')
    username = input()

    username_header = username + ":"

    print(f"{username}: ", end = '')
    msg = username_header + input()

    #print("msg: ", msg)

    while msg != username_header + DISCONNECT_MESSAGE:

        send_msg(msg)

        print(f"{username}: ", end = '')
        msg = username_header + input()
    
    #disconnect
    send_msg(username_header + DISCONNECT_MESSAGE)

client_loop()


