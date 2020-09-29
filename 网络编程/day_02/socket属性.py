from socket import *

sock = socket()

sock.bind(('192.168.1.100', 8888))
sock.listen(3)
cli, addr = sock.accept()
print('地址类型：', sock.family)
print('套接字类型', sock.type)
print('绑定地址', sock.getsockname())
print('描述符', sock.fileno())
print('客户端地址', cli.getpeername())  # 连接套接字才能调用
