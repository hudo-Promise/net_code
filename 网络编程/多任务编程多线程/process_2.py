from multiprocessing import Process
from time import  sleep
import os


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '------', os.getpid())


def th2():
    sleep(3)
    print("睡觉")
    print(os.getppid(), '------', os.getpid())


def th3():
    sleep(3)
    print("打豆豆")
    print(os.getppid(), '------', os.getpid())


def main():
    things = [th1, th2, th3]
    jobs = []
    for i in things:
        p = Process(target=i)
        jobs.append(p)
        p.start()

    for i in jobs:
        i.join()


if __name__ == '__main__':
    main()