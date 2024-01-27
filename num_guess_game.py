import random

print("Number Guessing game")
num_guess = int(input("Choose a number between 1 and 100: "))
random_num = random.randint(1, 100)
trials = 1

while True:
    if num_guess > random_num:
        print("Number should be lower!")
        num_guess = input("Guess a number between 1 and 100: ")
        num_guess = int(num_guess)
    elif num_guess < random_num:
        print("Number should be higher!")
        num_guess = input("Guess a number between 1 and 100: ")
        num_guess = int(num_guess)
    else:
        print(f"You got it right in {trials} tries!!! Good job!")
        ask_again = input("Do you want to play again? (y/n): ")
        trials = 1
        if ask_again == "y":
            random_num = random.randint(1, 100)
            num_guessguess = None
        else:
            print("Thank you for playing! Bye!")
            break
    trials += 1
