"""CP1404 Week 03 In-class demos: functions with testing."""
from string import ascii_lowercase


def main():
    # print(double(3))
    age = int(input("Age: "))
    # print("You may one day be {}".format(double(age)))
    doubled_age = double(age)
    print("You may one day be {}".format(doubled_age))


def double(number):
    """Double a number."""
    return number * 2


def count_letters(string):
    """Count the number of ASCII letters in string."""
    count = 0
    for character in string.lower():
        if character in ascii_lowercase:
            count += 1
    return count


def test_count_letters():
    # print("Expect 3. Got {}.".format(count_letters("abc")))
    # print("Expect 4. Got {}.".format(count_letters("abCD")))
    assert count_letters("abc") == 3
    assert count_letters("abCD-") == 4


def square(number):
    """Square a number."""
    return number ** 2


def test_square():
    test_values = [(6, 36), (5, 25)]
    for in_number, result in test_values:
        assert square(in_number) == result

# test_count_letters()
# test_square()
# main()
