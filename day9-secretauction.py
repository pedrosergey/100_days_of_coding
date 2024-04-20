# import some libraries

from ascii_images import day9_logo
import os

# create a function to add new bids to the dictionary

def add_new_bid(bid_dictionary):
    name = input("\nWhat is your name?: ").lower()
    bider = float(input("How much do you want to bider?: $"))

    bid_dictionary[name] = bider

# create a function to find the winner

def winners(bid_dictionary, bid_repetition):
    max_bid = max(bid_dictionary.values())
    number_of_max_bids = list(bid_dictionary.values()).count(max_bid)
    names_of_max_bidders = []

    for bidder in bid_dictionary:
        if bid_dictionary[bidder] == max_bid:
            names_of_max_bidders.append(bidder)
    
    if len(names_of_max_bidders) == 1:
        print(f"The winner is {names_of_max_bidders[0].capitalize()}")
    
    elif len(names_of_max_bidders) > 1:
        print(f"There was a tie, the auction should be repeated.")
        bid_repetition = input("Do you want to repeat the auction now? 'Yes' or 'No': ").lower()
        
# define some variables to control the flow of the code

new_bidders = True
bids = {}
bid_tie = "no"


print(day9_logo, "\nWelcome to the secret auction!")

# we create the main snippet of code

while new_bidders:

    add_new_bid(bids)

    more_bids = input("\nIs there anyone else that wants to place a bider? 'Yes' or 'No': ").lower()

    if more_bids == "yes":
        os.system("clear")
    
    else:
        new_bidders = False
        winners(bids, bid_tie)
        if bid_tie == 'yes':
            new_bidders = True

print("\nThanks so much for use this software to perform the secret auction!")
print("\nCongratulations to all the winners (if there were some)!! :)")


    



