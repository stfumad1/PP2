def myfunc(n):
    return abs(n-50)

list = [100 , 440, 50 , 12 , 66]
list.sort(key=myfunc)
print (list)