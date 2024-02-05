s = input("")


def reverse(s):
    word = s.split()
    return word[::-1]


result = reverse(s)
print(result)