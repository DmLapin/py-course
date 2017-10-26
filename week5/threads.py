from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed


def f(name):
    print('hello', name)


th = Thread(target=f, args=("Bob",))
th.start()
th.join()


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


th2 = PrintThread("Mike")
th2.start()
th2.join()


def fa(a):
    return a * a


# .shutdown() in exit
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(fa, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())
