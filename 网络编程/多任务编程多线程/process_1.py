import multiprocessing as mp
from time import sleep


def fun():
    print("子进程开始执行")
    sleep(3)
    print("子进程执行完毕")


p = mp.Process(target=fun)

p.start()
p.join()