# def reverser(s):
#     if len(s) <= 1:
#         return s
#     return reverser(s[1:]) + s[0]
#
#
# for t in ["Blah", "A Toyota's a Toyota", "HANNAH", "1234"]:
#     print(reverser(t))


def print_count_down(n):
    for i in range(n, -1, -1):
        print(i)


# print_count_down(4)

def factorial(n):
    # print("factorial of {} start".format(n))
    if n == 1 or n == 0:
        return 1
    result = n * factorial(n - 1)
    # print("factorial of {} end".format(n))
    return result


print(factorial(4))
