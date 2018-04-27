"""CP1404 2018-1 Week 09 Inheritance Demos."""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = 0

    def __str__(self):
        return "{} ({})".format(self.name, self.age)

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age


if __name__ == '__main__':
    p = Person("Jimmy", 32)
    print(p)
    p2 = Person("Nuno", 55)
    p3 = Person("Nuno", 55)
    print(p == p2)
    print(p.__eq__(p2))
    print(p2 == p3)
    assert p2 == p3
    print(p == "Nuno")
    print(p == 75.65)
    print(p == p)
