"""User class."""


class User:
    INITIAL_NUMBER_OF_TACOS = 5

    def __init__(self, name=""):
        self.name = name
        self.number_of_tacos = self.INITIAL_NUMBER_OF_TACOS
        self.score = 0

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.number_of_tacos)
