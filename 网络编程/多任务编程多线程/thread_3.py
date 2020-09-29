"""
自定义线程类
"""
from threading import Thread


class ThreadClass(Thread):
    def __init__(self, attr):
        self.attr = attr
        super().__init__()

    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()


t = ThreadClass("xxxxxxx")
t.start()
t.join()