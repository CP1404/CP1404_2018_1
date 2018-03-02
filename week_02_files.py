"""Week 02 files demo."""

file_in = open("text.txt")
# text = file_in.read()
# text = file_in.readlines()
for line in file_in:
    name, age = line.strip().split()
    print("{} is {} years old".format(name, age))
file_in.close()

file_out = open("results.txt", "w")
print("Thanks.", file=file_out)
file_out.close()
