import socket
import sys
import json

mydata = {"id" : 2018226522, "name": "Syafiqa" , "age" : "21"}
sendData = json.dumps(mydata)

s= socket.socket()
print("Socket sucessfully created")

port=8080

s.bind(('',port))
print("socket binded to" + str(port))

s.listen(5)
print("socket is listening ")

while True:
    c,addr = s.accept()
    print("Got connection from" + str(addr))

    c.sendall(bytes(sendData, encoding= "utf-8"))
    buffer = c.recv(1024)
    print(buffer)
c.close()
