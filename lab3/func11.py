def palindrome(s):
    return s == s[::-1]


s = input("")
result = palindrome(s)
print(result)