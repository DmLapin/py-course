# Создание процесса, модуль multiprocessing
import multiprocessing


def f(name):
    print("hello", name)


class PrintProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    p = multiprocessing.Process(target=f, args=("Bob",))
    p.start()
    p.join()

    p2 = PrintProcess("Mike")
    p2.start()
    p2.join()
