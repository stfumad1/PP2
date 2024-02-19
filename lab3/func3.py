numheads, numlegs = int(input("")), int(input(""))


def solve(numheads, numlegs):
   
    a = (numlegs / 2) - numheads
    b = numheads - ((numlegs / 2) - numheads)
    print(int(a), int(b))


solve(numheads, numlegs)