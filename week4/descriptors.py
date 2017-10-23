class Descriptor:
    def __get__(self, instance, owner):
        print('get')

    def __set__(self, instance, value):
        print('set')

    def __delete__(self, instance):
        print('delete')


class Class:
    attr = Descriptor()


instance = Class()
instance.attr
instance.attr = 10
del instance.attr
