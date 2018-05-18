from user import User
from team import Team


def main():
    names = ["Jimi", "Nuno", "Lincoln"]
    # users = []
    # for name in names:
    #     user = User(name)
    #     users.append(user)
    users = [User(name) for name in names]
    print(users)

    # print(test_user.INITIAL_NUMBER_OF_TACOS)
    # print(User.INITIAL_NUMBER_OF_TACOS)
    # print(test_user)


main()
