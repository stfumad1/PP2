import re
import os
path = "C:\Users\user\Desktop\123.txt"
with open ("C:\Users\user\Desktop\123.txt" , "r") as file:
    lines = file.readline()
    for i in lines:
        result = re.findall(r"[a-z]")
        print (result)
    