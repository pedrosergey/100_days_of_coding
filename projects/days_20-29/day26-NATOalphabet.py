# importing some libraries

import pandas as pd

df = pd.read_csv("data/day26_natophoneticalphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

input_word = input("Please, introduce the word that you want to code: ")

keep_asking = True

while keep_asking:
    try:
        code_word = [nato_alphabet[letter.upper()] for letter in input_word]
        if len(code_word) == 0:
            raise TypeError("A word should be typed!")
    except KeyError:
        print("Sorry, just letters in the alphabet are allowed.")
        input_word = input("Please, introduce a valid word: ")
    except TypeError as e:
        print(e)
        input_word = input("Please, introduce a valid word: ")
    else:
        print(code_word)
        keep_asking = False