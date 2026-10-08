import random

SecretNumber = random.randint(1, 5)
Attempts = 3

while Attempts > 0:
    guess = int(input("Guess the secret number (1-5): "))

    if guess == SecretNumber:
        print("You win, congrates")
        break

    Attempts = Attempts - 1

    if Attempts > 0:
        print("Wrong guess,try again.")
        print("Attempts left:", Attempts)
    else:
        print("Attempt over, good luck next time")
        print("The secret number was:", SecretNumber)