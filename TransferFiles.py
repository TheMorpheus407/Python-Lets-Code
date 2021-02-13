import socket
import os

file = r"G:\Tuts\Archive\Python LetsCodes\audio\long.wav"
host = "192.168.0.244"
sep = "#SEP#"
port = 1337
buffer = 1024

file_size = os.path.getsize(file)
if sep in file:
    print("WARNING! INVALID FILENAME!")
    exit(-1)
s = socket.socket()
s.connect((host, port))
s.send(f"{file}{sep}{file_size}".encode())

with open(file, "rb") as f:
    while True:
        file_bytes = f.read(buffer)
        if not file_bytes:
            break
        s.sendall(file_bytes)
s.close()

