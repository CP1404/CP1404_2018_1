"""Team class for Taco Users."""


class Team:
    def __init__(self):
        self.users = []

    def __repr__(self):
        return str(self.users)

    def add(self, user):
        self.users.append(user)
