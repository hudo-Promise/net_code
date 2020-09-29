from socket import *
import struct

sock = socket(AF_INET, SOCK_DGRAM)

sock.bind(('0.0.0.0', 8888))
f = open('xingxi.txt', 'a')

while True:
    data, addr = sock.recvfrom(1024)
    print(addr)
    if not data:
        break
    d = struct.unpack('i32sif', data)
    info = "%d %s %d %.2f\n" % (d[0], d[1].decode(), d[2], d[3])
    f.write(info)

f.close()
sock.close()
