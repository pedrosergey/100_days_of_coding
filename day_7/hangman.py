# import the necessary libraries

import random

# print the welcome message

print("Welcome to the Hangman game!\nWe wish you all the luck, you will need it!")

# set the words that we are going to use 

words_battery = ['leon', 'cat', 'drive']

random_word = random.choice(words_battery)

guessed_letter = input("Please, guess a letter: ").lower()

for char in random_word:
    if guessed_letter == char:
        print(True)

    else:
        print(False)

# we create a function that replace every character of the word with "_" 

# def redact_word(word):
    
#     redacted_word = ""

#     for i in range(len(word) - 1):
#         redacted_word += "_ "
#     redacted_word += "_"

#     return(redacted_word)

# def check_letter(letter, word):
    
#     for char in word:
#         if letter == char:
#             redact_word