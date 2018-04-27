from musician import Musician


class SpecialMusician(Musician):
    def __init__(self, name="", age=0):
        super().__init__(name, age)

    def play(self, duration):
        print("Here it comes...", end=" ")
        super().play(duration)
        print("!!")


if __name__ == '__main__':
    sm = SpecialMusician("Bob Dylan", 99)
    sm.play(2)
