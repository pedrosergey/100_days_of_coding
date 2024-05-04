# import the necessary libraries

import random
from data.day7_data import stages
from data.day7_words import word_list as words_battery
from data.ascii_images import day7_logo


# create some functions that we will use later on

def redact_word(word):
    redacted_list = []

    for i in range(len(word) - 1):
        redacted_list.append("_")

    redacted_list.append("_")

    return redacted_list


def transform_word_in_list(word):
    word_list = []

    for char in word:
        word_list.append(char)

    return word_list


# create a function to print the word

def print_word_list(word_list):
    redacted_word_str = ""

    for char in range(len(word_list) - 1):
        redacted_word_str += word_list[char]
        redacted_word_str += " "
    redacted_word_str += word_list[-1]

    print(redacted_word_str)


def check_input_letter(list_of_letters, redacted_list):

    letter = input("Please, guess a letter: ").lower()
    repetitions = list_of_letters.count(letter)

    if letter in redacted_list:
        print(f"You have already guessed {letter}.")

    elif repetitions == 0:
        print(f"{letter} is not in the word!")
        return 0

    else:
        for repetitions in range(repetitions):
            letter_index = list_of_letters.index(letter)
            list_of_letters[letter_index] = "*"
            redacted_list[letter_index] = letter
        print("Well done!")


# here is where the game starts

def hangman():

    print(day7_logo)
    print("Welcome to the Hangman game!\nWe wish you all the luck, you will need it!\n")
    print("The word that you need to guess is the following:")

    # define some variables

    random_word = random.choice(words_battery)

    redacted_word = redact_word(random_word)
    word_in_list = transform_word_in_list(random_word)
    lives = len(stages)
    missing_letters = redacted_word.count("_")

    while lives > 0 and missing_letters > 0:

        print_word_list(redacted_word)
        if check_input_letter(word_in_list, redacted_word) == 0:
            lives -= 1
            print(stages[lives])
        else:
            missing_letters = redacted_word.count("_")

    if missing_letters == 0:
        print(f"Congratulations, you win🎯! The guessed word was {random_word}!")
    else:
        print(f"The word was {random_word}. Your are hang! ☠️")

    if input("Do you want to play again? Type 'yes' or 'no': ").lower() == "yes":
        hangman()


hangman()

print("Thanks so much for having played this game!")
