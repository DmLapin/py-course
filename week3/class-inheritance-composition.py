class Pet:
    def __init__(self, name=None) -> None:
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed  # private

    def say(self):
        return "{0}: waw".format(self.name)

    def get_breed(self):
        return self.__breed


class ExportableDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter or ExportJson()

    def export(self):
        return self._exporter.export(self)


class ExportJson:
    def export(self, pet):
        return f"Exporting {pet} to json"


dog = Dog("Bro", "unknown")
print(dog.say())
print(issubclass(Dog, object), issubclass(Dog, Pet), isinstance(dog, Dog), isinstance(dog, Pet))

expDog = ExportableDog("Шарик", "Овчарка", ExportJson())
print(expDog.export())
