from itertools import permutations

def string_permutations():
   
    string = input("")

 
    perms = permutations(string)

    
   
    for perm in perms:
        print(''.join(perm))
        
string_permutations()