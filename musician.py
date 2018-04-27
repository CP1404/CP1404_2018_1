"""Musician class..."""
from person import Person


class Musician(Person):
    def __init__(self, name="", age=0):
        super().__init__(name, age)

    def play(self, duration):
        for i in range(duration):
            print("{} is playing ".format(self.name), end=' ')
        print()

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.name + other.name


if __name__ == '__main__':
    m = Musician("Nuno Bettencourt", 55)
    m.play(1)
