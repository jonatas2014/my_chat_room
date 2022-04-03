import socket
import threading

from constants import *

SERVER = '192.168.0.9' # ipv4 number, changes accordling with the machine
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    
    print(f"[NEW CONNECTION] {addr} connected.")
    username = ""

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:

            #message treatment
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            #collect username
            username = msg.split(":")[0]

            #show message
            print(f"{msg}")

            #user desconnection
            if msg.split(":")[1] == DISCONNECT_MESSAGE:
                connected = False
                print(f"User {username} has left the chat")

            #early way
            #print(f"[{addr}] {msg}")

            # uncomment the lin below to the server return the feedback: msg received to the client
            #conn.send("Msg received".encode(FORMAT))

    conn.close()


def braodcast_new_conexion():

    '''Inform all actives clients when a new client connect'''

    pass


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()