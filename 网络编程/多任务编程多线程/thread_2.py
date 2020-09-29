"""
线程传参
"""

from threading import Thread
from time import sleep


def fun(sec, name):
    print("线程传参")
    sleep(sec)
    print("%s 线程执行完毕" % name)


jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={'name': 'T%d' % i})
    jobs.append(t)
    t.start()


for i in jobs:
    i.join()

