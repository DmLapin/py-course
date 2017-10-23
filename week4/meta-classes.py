from abc import ABCMeta, abstractmethod


class Class:
    pass


obj = Class()
print(type(obj))
print(type(Class))


NewClass = type('NewClass', (), {})
print(NewClass)
print(NewClass())


class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class A(metaclass=Meta):
    pass


print('A.class_id: {}'.format(A.class_id))


class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        """Do it"""

