import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("Server started on hostname: ", host)
port = 8000
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print(addr, "has connected")
while 1:
    message = input(">>")
    message = message.encode()
    conn.send(message)
    print("Message sent")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(addr,": ", message)