import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

data=client.recv(4096)
print(data+"\n")
pin=input()
client.send(pin)
client.send("I am CLIENT\n")
from_server = client.recv(4096)
client.close()
print from_server
