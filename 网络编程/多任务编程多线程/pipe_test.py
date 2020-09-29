"""
Pipe 管道通信
实现进程间的通信
"""
from multiprocessing import Process, Pipe
import os, time

# 创建管道
pip1, pip2 = Pipe()


def fun(name):
    time.sleep(3)
    # 向管道写入内容
    pip1.send({name: os.getpid()})


def main():
    jobs = []
    for i in range(5):
        p = Process(target=fun, args=(i,))
        jobs.append(p)
        p.start()

    for i in range(5):
        # 读取管道
        data = pip2.recv()
        print(data)

    for i in jobs:
        i.join()


if __name__ == '__main__':
    main()

