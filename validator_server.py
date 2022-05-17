import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 65533))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} is good!")
#   clientsocket.send(bytes("It worked!", "utf-8"))
    clientsocket.sendall(b"Please enter your username")
    data = clientsocket.recv(1024)
    with open("user_info.json", "r") as data_pool:
        correct_info = json.load(data_pool)
    input_username = data.decode("utf-8")
    if input_username not in correct_info:
        clientsocket.sendall(b"Username not found")
        data = b"exit"
    else:
        clientsocket.sendall(b"Please enter your password")
        data = clientsocket.recv(1024)
        input_password = data.decode("utf-8")
        if input_password != correct_info[input_username]:
            clientsocket.sendall(b"Password incorrect")
            data = b"exit"
        else:
            clientsocket.sendall(b"Info entered is correct")
            data = b"exit"


