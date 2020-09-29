from socket import *
# 客户端

# 创建套接字
sock = socket(AF_INET, SOCK_STREAM)

# 发起连接
server_addr = ('127.0.0.1', 8888)
sock.connect(server_addr)

# 收发消息
while True:
    message = input('请输入要发送的消息：')
    if message == 'q':
        break
    sock.send(message.encode())
    data = sock.recv(1024)
    print('来自服务端的消息：', data.decode())

sock.close()

