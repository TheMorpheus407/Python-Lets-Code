import socket
import os

host = "0.0.0.0"
port = 1337
buffer = 1024
sep = "#SEP#"

s = socket.socket()
s.bind((host, port))
s.listen(5)
print("Server open...")
client_socket, address = s.accept()
print(f"{address} just connected...")
file, file_size = client_socket.recv(buffer).decode().split(sep)

file_name = os.path.basename(file)
file_size = int(file_size)
with open(file_name, "wb") as f:
    bytes_recv = client_socket.recv(buffer)
    while bytes_recv:
        f.write(bytes_recv)
        bytes_recv = client_socket.recv(buffer)
client_socket.close()
s.close()