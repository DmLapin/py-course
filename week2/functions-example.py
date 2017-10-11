from datetime import datetime


def get_seconds():
    """Return current seconds"""
    return datetime.now().second


print(get_seconds())
print(get_seconds.__doc__)
print(get_seconds.__name__)


def change_list(list_var):
    list_var.append('appended')


global_list = [1, 2]
print(global_list)
change_list(global_list)
print(global_list)


def say_hello(greeting, name):
    print('{}, {}!'.format(greeting, name))


say_hello('Hello', 'John')
say_hello(name='Alex', greeting='Bye')


def float_args(*args, **kwargs):
    print(args, kwargs)


float_args(1, 2, a=3, b=4)
