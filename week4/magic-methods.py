class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


a = Singleton()
b = Singleton()
print(a is b)


class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.params = dict()

    def __str__(self) -> str:
        return '{} <{}>'.format(self.name, self.email)

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email

    def __getattr__(self, item):
        return 'No attr'

    def __getattribute__(self, item):
        if item == 'name':
            print('name attr access')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('setting')
        object.__setattr__(self, key, value)

    def __call__(self, *args, **kwargs):
        print('calling')

    def __getitem__(self, item):
        if item in self.params:
            return self.params[item]
        else:
            return 'No such key'

    def __setitem__(self, key, value):
        self.params[key] = value


vas = User('Vasya', 'vas@mail.com')
bill = User('Bill', 'vas@mail.com')
print(vas)  # __str__
print(vas == bill)  # __eq__
print(hash(vas), hash(bill))  # __hash__
print(vas.noattr, vas.name)  # __getattr__, __getattribute__
bill()  # __call__
print(vas['city'])  # __getitem__
vas['city'] = 'Moscow'  # __setitem__
print(vas['city'])
