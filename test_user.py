"""Simple tests for the User class"""
from user import User


def run_tests():
    user = User()
    print("number should be 5; is {}".format(user.number_of_tacos))
    assert user.number_of_tacos == 5, "problem"

    user2 = User("Ben")
    print(user2)


run_tests()
