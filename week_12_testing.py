"""CP1404 2018-1 Week 12. Demos of testing."""
import doctest
from string import ascii_lowercase


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


def create_empty_list():
    return []


# x = create_empty_list()
# assert x == []

def is_adult(age):
    """
    Determine if age corresponds to an adult or not.
    >>> is_adult(18)
    True
    >>> is_adult(2)
    False
    """
    return age >= 18


def get_middle(values):
    """
    >>> get_middle([1, 2])
    1
    >>> get_middle([1, 2, 3])
    2
    >>> get_middle('abc')
    'b'
    """
    length = len(values)
    index = length // 2
    if length % 2 == 0:
        index -= 1

    return values[index]


doctest.testmod()
