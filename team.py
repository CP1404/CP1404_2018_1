"""Team class for Taco Users."""


class Team:
    def __init__(self):
        self.users = []

    def __repr__(self):
        return str(self.users)

    def add(self, user):
        self.users.append(user)

    def get_leader(self):
        highest_score = -1
        leader = None
        for user in self.users:
            if user.score > highest_score:
                highest_score = user.score
                leader = user
        return leader

    def get_total_score(self):
        return sum([user.score for user in self.users])
