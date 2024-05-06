# import the necessary libraries

import random
import os
from data.day14_data import data
from data.ascii_images import day14_vs as vs, day14_logo as logo

# define the function to pick a name from the list and return it

def pick_a_name(data_list):
    '''Pick a element from a list and remove this element from the actual list'''

    random_pick = random.randint(0, len(data_list) - 1)
    random_person = data_list[random_pick]

    return random_person

def comparison(data, person_a, person_b, score):
    """Perform a comparison between two people"""
    print(f"Your current score is: {score}")

    print(f"\nCompare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']} from {person_b['country']}.")

    followers_a = person_a['follower_count']
    followers_b = person_b['follower_count']

    guess = input("Who do you think have more followers? 'A' or 'B': ").lower()

    if followers_a > followers_b and guess == "a":
        print(f"\nYou are right. {person_a['name']} has {person_a['follower_count']} million followers and {person_b['name']} has {person_b['follower_count']} million.")
        return person_a
    elif followers_a < followers_b and guess == "b":
        print(f"\nYou are right. {person_a['name']} has {person_a['follower_count']} million followers and {person_b['name']} has {person_b['follower_count']} million.")
        return person_b
    else:
        print(f"\nYou are wrong! {person_a['name']} has {person_a['follower_count']} million followers and {person_b['name']} has {person_b['follower_count']} million.")
        return "c"


# print the start of the game

print(logo, "\nWelcome to this guessing game!")


# start the game

def play_comparison():

    score = 0

    person_a = pick_a_name(data)
    person_b = pick_a_name(data)

    data.remove(person_a)
    data.remove(person_b)

    result = comparison(data, person_a, person_b, score)

    while result != "c":
        score += 1
        person_a = person_b
        person_b = pick_a_name(data)
        data.remove(person_b)
        result = comparison(data, person_a, person_b, score)

    if result == "c":
        print("You have lost!")

    print(f"\nYour final score was {score}!")
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()

    if play_again == 'y':
        os.system('clear')
        play_comparison()


play_comparison()

print("Thanks for having fun with us! See you next time <|3")