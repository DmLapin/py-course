class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        with open('descriptor-log.txt', 'w') as f:
            f.write(str(value))

        self.amount = value


class Account:
    amount = ImportantValue(100)


bill = Account()
bill.amount = 150
john = Account()
print(john.amount)
