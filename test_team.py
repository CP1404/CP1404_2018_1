from team import Team
from user import User


def run_tests():
    team1 = Team()
    user1 = User("Jenny")
    print(team1)
    assert team1.users == []
    assert not team1.users

    team1.add(user1)
    assert team1.users
    print(team1.users)


run_tests()
