"""
Chat room

"""

from socket import *
import os, sys

# 服务器地址
ADDR = ('0.0.0.0', 8888)
user = {}


def do_login(sock, name, addr):
    if name in user or "管理员" in name:
        sock.sendto("该用户已经存在".encode(), addr)
        return
    sock.sendto(b'OK', addr)
    msg = "欢迎%s进入聊天室" % name
    for i in user:
        sock.sendto(msg.encode(), user[i])
    user[name] = addr


# 聊天
def do_chat(sock, name, text):
    msg = "%s : %s" % (name, text)
    for i in user:
        if i != name:
            sock.sendto(msg.encode(), user[i])


# 退出聊天
def do_quit(sock, name):
    msg = "%s退出了聊天室" % name
    for i in user:
        if i != name:
            sock.sendto(msg.encode(), user[i])
        else:
            sock.sendto(b'EXIT', user[i])
        del user[name]


# 请求接收
def recv_request(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        msg = data.decode().split(' ')
        if msg[0] == 'L':
            do_login(sock, msg[1], addr)
        elif msg[0] == 'C':
            text = ' '.join(msg[2:])
            do_chat(sock, msg[1], text)
        elif msg[0] == 'Q':
            do_quit(sock, msg[1])


# 创建网络连接
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        while True:
            msg = input("管理员消息")
            msg = "C 管理员消息 " + msg
            sock.sendto(msg.encode(), ADDR)
    else:
        recv_request(sock)  # 处理客户端请求


if __name__ == '__main__':
    main()
