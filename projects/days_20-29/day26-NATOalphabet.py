# importing some libraries

import pandas as pd

df = pd.read_csv("data/day26_natophoneticalphabet.csv")

nato_alphabet = {word.letter:word.code for (letter, word) in df.iterrows()}

input_word = input("Please, introduce the word that you want to code: ")
code_word = [nato_alphabet[letter.upper()] for letter in input_word]

print(code_word)
