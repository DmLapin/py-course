import time


with open('context-manager.txt', 'w') as f:
    f.write('It\'s works')


class open_file:
    def __init__(self, filename, mode) -> None:
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        if exc_type == ZeroDivisionError:
            print('zero division detected')
            return True


with open_file('context-manager-own.txt', 'w') as f:
    f.write('It\'s also works!')

with open_file('context-manager-own.txt', 'r') as f:
    print(f.read())
    1 / 0


class timer:

    def __init__(self) -> None:
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Elapsed: {}'.format(self.current_time()))


with timer() as t:
    time.sleep(1)
    print('Current time: {}'.format(t.current_time()))
    time.sleep(1)
