from socket import *

mySock = socket(AF_INET,SOCK_DGRAM)
mySock.bind(('', 25565))

while True:
    message, clientAddress = mySock.recvfrom(2048)
    message = message.decode()
    print(message)
    mySock.sendto("got it".encode(), clientAddress)
