tuuple = tuple(map(str, input().split()))
def alltrue(t):
    return all(map(bool , t))

if alltrue(tuuple):
    print ("TRUE")
else:
    print ("FALSE")