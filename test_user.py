"""Simple tests for the User class"""
from user import User


def run_tests():
    user1 = User()
    print("number should be 5; is {}".format(user1.number_of_tacos))
    assert user1.number_of_tacos == 5, "problem"

    user2 = User("Ben")
    print(user2)

    #     test give_tacos
    user1.give_tacos(user2, -7)
    print(user1)
    print(user2)


run_tests()
