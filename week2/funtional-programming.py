from functools import reduce
from functools import partial


# function as callback
def double_num(a):
    return a * 2


num_list = [1, 4, 8]
print(num_list)
doubled_list = list(map(double_num, num_list))
print(doubled_list, num_list)

# lambda
print(list(filter(lambda x: x > 0, range(-3, 5))))


def stringify(num_list):
    return list(map(str, num_list))


print(stringify([2, 9, 7]))


# reduce
def multiply(a, b):
    return a*b


print(reduce(multiply, [1, 2, 3, 4]))


# partial
def multiplier(a, coef):
    return a * coef


mul3 = partial(multiplier, coef=3)
mul2 = partial(multiplier, coef=2)
print(mul2(5))
print(mul3(5))


# list comprehensions
square_list = [number ** 2 for number in range(10)]
square_map = {number: number ** 2 for number in range(10)}
print(square_list, square_map)

