import random
# 2 + 2 python file
def play_game():
    secret = random.randint(1, 100)   # number to guess
    attempts = 0
    guessed = False

    print("Guess the number between 1 and 100!")

    while not guessed:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Congratulations! You guessed it in", attempts, "tries.")
            guessed = True

play_game()

