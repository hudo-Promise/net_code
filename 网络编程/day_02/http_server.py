"""
http 功能演示

将网页发送给浏览器展示

"""

from socket import *

# 搭建tcp网路


def main():
    sock= socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', 8000))
    sock.listen(3)
    print('Listen the port 8000...')
    while True:
        connfd, addr = sock.accept()
        handle(connfd)


def handle(conn):
    print('Request from', conn.getpeername())
    request = conn.recv(4096)
    if not request:
        return
    request_line = request.splitlines()[0].decode()
    info = request_line.split(' ')[1]
    if info == '/':
        f = open("index.html", 'r', encoding='UTF-8')
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += '\r\n'
        response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found \r\n"
        response += "Content-Type: text/html\r\n"
        response += '\r\n'
        response += "<h1>Sorry...</h1>"
    conn.send(response.encode())


if __name__ == '__main__':
    main()
