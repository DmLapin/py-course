def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


for number in even_range(0, 10):
    print(number)


print('')


def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value:
            break
        total += value


generator = accumulator()
print(next(generator))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print(next(generator))
