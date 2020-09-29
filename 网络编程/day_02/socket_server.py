import socket
# 服务端
# 创建流式套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sock.bind(('0.0.0.0', 8888))

# 设置监听
sock.listen(5)

# 等待处理客户端连接
while True:
    print('Waiting for connect......')
    try:
        conn, addr = sock.accept()
    except KeyboardInterrupt:
        print('退出服务')
        break

# 收发消息
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("接收到的消息：", data.decode())
        n = conn.send(b'Receive your message')
        print('数据发送完成')
    conn.close()
# 关闭套接字
sock.close()


