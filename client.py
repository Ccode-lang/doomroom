import socket
import sys
from subprocess import Popen, PIPE
import os
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(20)

def connect(coninfo):
    client = ""
    if os.path.isfile("chocolate-doom.exe"):
        client = "chocolate-doom.exe"
    elif os.path.isfile("crispy-doom.exe"):
        client = "crispy-doom.exe"
    if os.path.isfile("chocolate-doom"):
        client = "chocolate-doom"
    elif os.path.isfile("crispy-doom"):
        client = "crispy-doom"

    process = Popen([os.path.join(".", client), '-connect', coninfo[0], "-port", coninfo[1]] + coninfo[2].split(" "), stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    print(stdout.decode())

def main():
    if sys.argv[1] == "register":
        sock.connect((sys.argv[2], 3425))
        sock.send(f"reg:{sys.argv[3]}:{sys.argv[4]}:{sys.argv[5]}:{sys.argv[6]}".encode())
    elif sys.argv[1] == "connect":
        sock.connect((sys.argv[2], 3425))
        sock.send(f"con:{sys.argv[3]}".encode())
        coninfo = sock.recv(1024).decode().strip().split(":")
        if coninfo[0] == "nrd":
            print("The room you have requested is not defined.")
            return
        print(coninfo)
        connect(coninfo)
    elif sys.argv[1] == "list":
        sock.connect((sys.argv[2], 3425))
        sock.send("lst".encode())
        rooms = json.loads(sock.recv(1024).decode())
        for key in rooms:
            print(f"{key}: {rooms[key]}")


main()
sock.close()