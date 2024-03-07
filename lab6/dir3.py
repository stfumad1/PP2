import os

def c(pathh):
    if os.path.exists(pathh):
        print(f"path {pathh} exists")
        dirname, filename = os.path.split(pathh)
        print(f"filename : {filename}")
        print(f"dirname : {dirname}")
    else:  
        print(f"path {pathh} does not exist.")

input_path = input("Enter a path: ")
c(input_path)
