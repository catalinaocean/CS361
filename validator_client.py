import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 65533))

while True:
    data = s.recv(1024)
    if data == b"exit":
        break
    print(data.decode("utf-8"))
    input_info = input()
    b_input = input_info.encode()
    s.sendall(b_input)
