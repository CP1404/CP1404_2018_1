"""Week 04 demo code - lists."""

string = input("Enter a string: ")
letters = list(string)
for letter in sorted(letters, reverse=True):
    print(letter)

# list comprehension examples...
numbers = list(range(20))
print(numbers)

# the for-loop way:
specials = []
for number in numbers:
    if number % 2 == 0:
        specials.append((number, number * 2))
print(specials)

# using a list comprehension:
values = [(number, number * 2) for number in numbers if number % 2 == 0]
print(values)

# if we don't need to store the values,
# we can use round brackets and get a "generator expression" instead of a list:
for value in ((number, number * 2) for number in numbers if number % 2 == 0):
    print(value)
