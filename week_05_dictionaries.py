"""CP1404 Week 05 - Dictionaries demos."""


def main():
    name_to_number = {'jess': 42, 'adam': 6, 'derek': 890, 'sally': 140}

    for thing in name_to_number:
        print(thing)

    print(name_to_number)
    for name in name_to_number:
        print(name, name_to_number[name])

    name = input("Name: ")
    age = int(input("Age: "))
    name_to_number[name] = age

    for name, number in name_to_number.items():
        print("{:10} - {:10}".format(name, number))

    # dictionary comprehension example
    print(name_to_number)
    new_d = {k[0]: name_to_number[k] // 2 for k in name_to_number}
    print(new_d)


main()
