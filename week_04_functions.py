"""Week 04 demo code - functions: scope, parameters."""


def main():
    x = 5
    numbers = [1]
    do_stuff(x, numbers, -23)
    print("\nmain: ")
    print(x)
    print(id(numbers))
    print(numbers)


def do_stuff(x, things, z=500):
    print("do_stuff: ")
    print("z is {}".format(z))
    x = x * 2
    things.append(50)
    print(x)
    print(id(things))
    print(things)


main()
