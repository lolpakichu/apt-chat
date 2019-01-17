import socket
import sys
import time
import threading

s = socket.socket()
host = socket.gethostname()
print("Server started on hostname: ", host)
port = 8000
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print(addr, "has connected")
def send_Messages():
    while 1:
        message = input(">>")
        message = message.encode()
        conn.send(message)
        print("Message sent")
def receive_Messages():
    while True:
        incoming_message = conn.recv(1024)
        incoming_message = incoming_message.decode()
        print(">> Client: ", incoming_message)

incoming_thread = threading.Thread(target=receive_Messages)
incoming_thread.start()
send_thread = threading.Thread(target=send_Messages)
send_thread.start()