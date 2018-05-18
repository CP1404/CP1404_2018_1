import os

longest_file = ''
longest_length = 0
for filename in os.listdir('.'):
    # print(filename)
    try:
        with open(filename) as file:
            length = len(file.read())
            if length > longest_length:
                longest_length = length
                longest_file = filename
    except UnicodeDecodeError:
        print("Error decoding {}".format(filename))
    except IsADirectoryError:
        pass
print(longest_file, longest_length)
