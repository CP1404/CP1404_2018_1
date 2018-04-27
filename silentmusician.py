from musician import Musician


class SilentMusician(Musician):
    def __init__(self, name="", age=0):
        super().__init__(name, age)

    def play(self, duration):
        print("It's {}... Shhh...".format(self.name))


if __name__ == '__main__':
    m = SilentMusician("John Cage")
    print(type(m))
    print(isinstance(m, SilentMusician))
    print(isinstance(m, str))
    print(isinstance(m, Musician))
    print(isinstance(m, object))
    print(len(m))
