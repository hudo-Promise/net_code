from socket import *


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Msg>>")
    if not data:
        break
    sock.sendto(data.encode(), ADDR)
    msg, addr = sock.recvfrom(1024)
    print("From server", msg.decode())

sock.close()