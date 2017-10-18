class Human:

    def __init__(self, name, age=0) -> None:
        self.name = name
        self.age = age

    def __del__(self):
        print("Bye!")

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self.name}")


class Robot:
    """Class doc"""


class Planet:
    """Planet class"""

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __str__(self) -> str:
        return 'To string: ' + self.name

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)


print(Robot)
planet = Planet("Earth")
print(planet, planet.name, sep=', ')
planet.name = 'Changed Earth'
print(planet.name)
print(Planet.count)
mars = Planet("Mars")
print(Planet.count, mars.count)

human = Human('Somebody')
del human

print(planet.__dict__)
planet.mass = 15
print(planet.__dict__)

bob = Human("Bob")
mars.add_human(bob)
print(mars.population)
bob.say_name()
