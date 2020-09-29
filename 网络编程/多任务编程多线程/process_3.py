from multiprocessing import Process
import time


def worker(sec, name):
    for i in range(3):
        time.sleep(sec)
        print("I am %s" % name)
        print("I am working...")


if __name__ == '__main__':
    # p = Process(target=worker, args=(2, "Baron"))
    # 关键字传参
    p = Process(target=worker, kwargs={'name': 'baron', 'sec': 2})
    p.start()
    p.join()
