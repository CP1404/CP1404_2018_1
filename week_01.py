"""Week 01 demo code - basic bits and pieces."""

from random import randint

age = int(input("Age: "))
print("You are", age)

random_number = randint(1, 20)

# DRY principle - we don't want to duplicate the final print in the if/else, only store the difference
if random_number == 1:
    years_string = "year"
else:
    years_string = "years"

# later, we will come back to this kind of printing more nicely with string formatting
print("In", random_number, years_string, ", you will be", age + random_number)
