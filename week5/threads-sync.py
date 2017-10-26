from queue import Queue
from threading import Thread, RLock


def worker(q, n):
    while True:
        item = q.get()
        if item is None:
            break
        print("process data:", n, item)


q = Queue(5)
th1 = Thread(target=worker, args=(q, 1))
th2 = Thread(target=worker, args=(q, 2))
th1.start(); th2.start()

for i in range(50):
    q.put(i)

q.put(None); q.put(None)
th1.join(); th2.join()


# Синхронизация потоков, race condition
class Point(object):
    def __init__(self, x, y):
        self.mutex = RLock()
        self.set(x, y)

    def get(self):
        with self.mutex:
            return (self.x, self.y)

    def set(self, x, y):
        with self.mutex:
            self.x = x
            self.y = y


# use in threads
my_point = Point(10, 20)
my_point.set(15, 10)
print(my_point.get())


# Синхронизация потоков, блокировки
a = RLock()
b = RLock()


def foo():
    try:
        a.acquire()
        b.acquire()
    finally:
        a.release()
        b.release()
