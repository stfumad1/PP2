import random

def guess_the_number():
    name = input("Hello! What is your name? \n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    
    secret_number = random.randint(1, 20)
    num_guesses = 0
    while True:
        guess = int(input("Take a guess: "))
        num_guesses += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

guess_the_number()