from project_data.ascii_images import day12_logo
import random
import os

print(day12_logo, "\nWelcome to Guess the Number, we hope you get fun! :D")
print("You should guess the number between 1 and 100 (inclusive), before running out of attempts.")


def guessing_a_number(random_number, attempts_lefts):
    """Return the number that the user has guessed."""
    print(f"You have {attempts_lefts} attempts left.")
    number = int(input("Please, guess a number: "))
    if random_number == number:
        print(f"Congratulations, the number was {number} you have won!🎯")
        return -1
    elif random_number > number:
        attempts_lefts -= 1
        if attempts_lefts > 0:
            print(f"You guessed {number}. The secret number is larger.")
        else:
            print(f"You guessed {number}. The correct number was {random_number}")
        return attempts_lefts
    elif random_number < number:
        attempts_lefts -= 1
        if attempts_lefts > 0:
            print(f"You guessed {number}. The secret number is smaller.")
        else:
            print(f"You guessed {number}. The correct number was {random_number}!")
        return attempts_lefts


def guess_a_number():
    attempts = 0
    end_game = False
    difficulty = input("Please, choose 'easy' or 'hard' to start the game: ").lower()

    while difficulty not in ["easy", "hard", "exit"]:
        difficulty = input("Please, choose 'easy' or 'hard' to start the game. Type 'exit' to leave: ").lower()

    selected_number = random.choice(range(1, 101))

    if difficulty == 'hard':
        attempts = 5
    elif difficulty == 'easy':
        attempts = 10
    else:
        end_game = True

    # execute the function until the user run out of attempts

    while attempts > 0 and not end_game:
        attempts = guessing_a_number(selected_number, attempts)

        if attempts == 0:
            print("Sorry, you run out of attempts, you lost ☠!")
            end_game = True

    if input("Do you want to keep playing? Press 'y' or 'n': ").lower() == "y":
        os.system("clear")
        guess_a_number()


guess_a_number()

print("I hope all of you had fun playing this wonderful game!:D")
