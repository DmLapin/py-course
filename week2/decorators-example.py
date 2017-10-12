def decorator(func):
    def new_func():
        print('Bye')
    return new_func


@decorator
def decorated():
    print('Hello')


print(decorated.__name__)
decorated()


def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        print('Logged')
        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


print(summator([2, 3]))


def logger_with_param(param):
    def decorator_inner(func):
        def wrapped(num_list):
            result = func(num_list)
            print('Logged param {}'.format(param))
            return result
        return wrapped
    return decorator_inner


@logger_with_param('NICE')
def summator_param(num_list):
    return sum(num_list)


print(summator_param([3, 7]))
