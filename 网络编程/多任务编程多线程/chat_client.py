"""
Chat room

"""

from socket import *
import os, sys


# 服务器地址
ADDR = ('127.0.0.1', 8888)


def send_msg(sock, name):
    while True:
        try:
            text = input("发言：")
        except KeyboardInterrupt:
            text = 'quit'
        if text == 'quit':
            msg = " Q " + name
            sock.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        sock.sendto(msg.encode(), ADDR)


def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode())


# 创建网络连接
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input('请输入你的姓名：')
        msg = "L " + name
        sock.sendto(msg.encode(), ADDR)
        data, addr = sock.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(sock, name)
    else:
        recv_msg(sock)


if __name__ == '__main__':
    main()


