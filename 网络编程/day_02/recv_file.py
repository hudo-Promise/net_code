from socket import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)

c, addr = s.accept()
print("connect from...", addr)

f = open('', 'wb')
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()
