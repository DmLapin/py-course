class Book:

    def __init__(self, title, author, year=None) -> None:
        self.title = title
        self.author = author
        self._year = year

    def __str__(self) -> str:
        return f"{self.title} ({self.author})"

    year = property()

    @classmethod
    def from_string(cls, string):
        title_author = string.split(":")
        return cls(title_author[0], title_author[1])

    @staticmethod
    def is_title_valid(title):
        return 0 < len(title) < 50

    @year.setter
    def year(self, value):
        if value <= 0:
            self._year = 2017
        else:
            self._year = value

    @year.getter
    def year(self):
        return self._year


war_peace = Book.from_string("Война и мир:Л. Толстой")
war_peace2 = war_peace.from_string("Путешествие:Гоголь")
print(war_peace, war_peace2)
print(Book.is_title_valid('Война и мир'), war_peace.is_title_valid(''))
war_peace.year = 0
print(war_peace.year)
