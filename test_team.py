from team import Team
from user import User


def run_tests():
    team1 = Team()
    user1 = User("Jenny")
    user2 = User("Lukas")
    number_to_give = 3
    user1.give_tacos(user2, number_to_give)
    print(team1)
    assert team1.users == []
    assert not team1.users

    team1.add(user1)
    team1.add(user2)
    assert team1.users
    print(team1.users)

    print(team1.get_leader())

    print("Total score expected: {}; got {}".format(number_to_give, team1.get_total_score()))
    assert team1.get_total_score() == number_to_give


run_tests()
