import socket
import atexit


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 3425))
sock.listen()


servers = {}

def onexit():
    print("closing")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

atexit.register(onexit)
while True:
    clientsock, clientaddr = sock.accept()
    clientsock.settimeout(3)
    try:
        msg = clientsock.recv(1024).decode().strip().split(":")
    except:
        print(f"Error recieving from {clientaddr}")
    if msg[0] == "reg":
        roomcode = msg[1]
        roomip = msg[2]
        roomport = msg[3]
        roomoptions = msg[4]
        servers[roomcode] = [roomip, roomport, roomoptions]
        print(f"Registered room {roomcode} with data: {servers[roomcode]}")
    elif msg[0] == "con":
        roomcode = msg[1]
        if roomcode in servers:
            room = servers[roomcode]
            print(f"Sending room {roomcode} {room} to {clientaddr}")
            try:
                clientsock.send(f"{room[0]}:{room[1]}:{room[2]}".encode())
            except:
                print(f"Error sending room information to {clientaddr}")
        else:
            try:
                print(f"Sending no room defined error to {clientaddr}")
                clientsock.send("nrd".encode())
            except:
                print(f"Error sending no room defined to {clientaddr}")
    clientsock.close()