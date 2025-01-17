from art import logo
import random

print(logo)

def game(num, attempt):
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == num:
            print(f"You got it! The answer was {num}")
            return True

        elif guess != num and guess > num:
            print("Too high.")
            attempt -= 1
            if attempt == 0:
                print("You've run out of guesses. Refresh the page to run again")
                return False
            else:
                print("Guess again.")

        elif guess != num and guess < num:
            print("Too low.")
            attempt -= 1
            if attempt == 0:
                print("You've run out of guesses. Refresh the page to run again")
                return False
            else:
                print("Guess again.")

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
number = random.randint(1, 100)

level_of_game = input("Choose a difficulty. Type 'easy' or 'hard':  ")

if level_of_game == "easy":
    round = 10
    game(number, round)
elif level_of_game == "hard":
    round = 5
    game(number, round)

