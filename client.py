import socket
import sys
import time
import threading
 
s = socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8000
s.connect((host,port))
print(" Connected to chat server")
def send_Messages():
    while 1:
        message = input(str(">>"))
        message = message.encode()
        s.send(message)
        print("message has been sent...")
        print("")
def receive_Messages():
    while True:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print(" Server: ", incoming_message)
        print("")

incoming_thread = threading.Thread(target=receive_Messages)
incoming_thread.start()
send_thread = threading.Thread(target=send_Messages)
send_thread.start()
