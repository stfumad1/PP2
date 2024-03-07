def countuplow(s):
    upper = sum (1 for char in s if char.isupper())
    low = sum(1 for char in s if char.islower())
    return upper , low

s = input("")
upper , low = countuplow(s)
print (upper)
print (low)