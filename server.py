import socket
import threading

from constants import *

SERVER = '192.168.0.9' # ipv4 number, changes accordling with the machine
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{msg}")

            #early way
            #print(f"[{addr}] {msg}")

            # uncomment this line to server return the feedback: msg received
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