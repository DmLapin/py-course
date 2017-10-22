import os.path
import traceback


class MyClass:
    pass


d = {"foo": "bar"}
obj = MyClass()

try:
    obj.foo
    1 / 0
    d["x"]
except (AttributeError, KeyError):
    print("Ошибка")
except ZeroDivisionError:
    print("Ошибка деления на 0")
else:
    print("Нет ошибок")


try:
    filename = '/not/exists'
    if not os.path.exists(filename):
        raise ValueError("Файл не существует", filename)
except ValueError as err:
    message, fname = err.args[0], err.args[1]
    print(message, fname)
    # print(traceback.print_exc())

# Assertions
assert True
assert 1 == 0
