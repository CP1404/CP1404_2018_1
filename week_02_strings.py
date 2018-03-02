"""Week 02 Demos - strings and things."""
from string import ascii_lowercase

# From warmup - standard while loop format
# total, count = 0, 0
# age = int(input("? "))
# while age >= 0:
#     total += age
#     count += 1
#     age = int(input("? "))
#
# print(total / count)


text = "playing jazz vibe chords quickly excites my wife"

# Write down the values of these expressions:
text[0]
text[-1]
text[5:10]
text[10:5:-1]
text.find(' ')
text.upper()[:10]
text[text.find('z'):text.find('e')].title()
text.isalpha()
text.split()

# String formatting
# From "do this now" in the notes:
print("{0} ({2}) has ${1:.2f}".format("Monty", 73.6, "male"))

for i in range(0, 13, 3):
    print("{:0=2}".format(i))

# Write a loop that prints the count of every letter, alphabetically
for letter in ascii_lowercase:
    print("{} {:2}".format(letter, text.count(letter)))

# Challenge: print all of the words in text with their lengths - nicely aligned
words = text.split()
max_length = max(len(word) for word in words)
for word in words:
    print("{:{}} {:2}".format(word, max_length, len(word)))
