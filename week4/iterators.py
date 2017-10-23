iterator = iter([1, 5, 7])
print(next(iterator))


class CustomIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result


for num in CustomIterator(3, 8):
    print(num)

