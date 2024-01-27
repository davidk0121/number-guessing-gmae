import random

print("Number Guessing game")
num_guess = int(input("Choose a number between 1 and 100: "))
random_num = random.randint(1, 100)
trials = 0

while True:
    if num_guess > random_num:
        print("Number should be lower!")
    elif num_guess < random_num:
        print("Number should be higher!")
    else:
        print(f"You got it right in {trials} tries!!! Good job!")
        ask_again = input("Do you want to play again? (y/n): ")
        if ask_again.lower() == "y":
            random_num = random.randint(1, 100)
            num_guess = None
            trials = 0  # Reset
        else:
            print("Thank you for playing! Bye!")
            break

    trials += 1
    num_guess = input("Guess a number between 1 and 100: ")
    num_guess = int(num_guess)
