"""User class."""


class User:
    INITIAL_NUMBER_OF_TACOS = 5

    def __init__(self, name=""):
        self.name = name
        self.number_of_tacos = self.INITIAL_NUMBER_OF_TACOS
        self.score = 0

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.number_of_tacos)

    def give_tacos(self, other_user, number_to_give):
        if self.number_of_tacos < number_to_give:
            number_to_give = self.number_of_tacos
        elif number_to_give < 0:
            number_to_give = 0
        self.number_of_tacos -= number_to_give
        other_user.score += number_to_give
