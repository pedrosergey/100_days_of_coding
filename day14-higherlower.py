# import the necessary libraries

import random
from day14_data import data
from ascii_images import day14_vs as vs, day14_logo as logo

# define the functions to pick a name from the list and print it

def pick_a_name(data_list):
    '''Pick a element from a list and remove this element from the actual list'''

    random_pick = random.randint(0, len(data_list) - 1)
    random_person = data_list[random_pick]

    data_list.pop(random_pick)

    

    return random_person

def first_comparison():

    person_a = pick_a_name(data)
    person_b = pick_a_name(data)

    print(f"Compare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']} from {person_b['country']}.")

    followers_a = person_a['follower_count']
    followers_b = person_b['follower_count']

    if followers_a > followers_b:
        return person_a
    elif followers_a < followers_b:
        return person_b
    else:
        return "c"

# print the start of the game

# print(logo)


# define some initial variables 


# start the game

print(comparison())
