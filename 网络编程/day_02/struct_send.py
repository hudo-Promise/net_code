from socket import *
import struct

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    Id = int(input("ID>>"))
    if Id == '':
        break
    name = input("NAME>>").encode()
    age = int(input("AGE>>"))
    score = float(input("SCORE>>"))
    data = struct.pack('i32sif', Id, name, age, score)
    sock.sendto(data, ADDR)
    # msg, addr = sock.recvfrom(1024)
    # print("From server", msg.decode())

sock.close()