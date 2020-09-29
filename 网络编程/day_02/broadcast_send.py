# 发送广播
from socket import *
from time import sleep

# 广播地址
dest = ('192.168.1.100', 9999)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
data = """广播内容"""

while True:
    sleep(2)
    s.sendto(data.encode(), dest)

s.close()


