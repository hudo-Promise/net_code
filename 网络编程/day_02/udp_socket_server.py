from socket import *

sock = socket(AF_INET, SOCK_DGRAM)

server_addr = ('0.0.0.0', 8888)
sock.bind(server_addr)

while True:
    data, addr = sock.recvfrom(1024)
    if data == None:
        break
    print("收到的消息：", data.decode())
    sock.sendto(b'Thanks', addr)

sock.close()