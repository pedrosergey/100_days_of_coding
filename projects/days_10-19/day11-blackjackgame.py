############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# import some libraries

from data.ascii_images import day11_logo
import random
import os

# we define some variables

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

keep_playing = "y"

print(day11_logo, "\nWelcome to our Blackjack game. Are you ready to have fun?")
keep_playing = input("Do you want to start a game? Type 'y' or 'n': ").lower()

while keep_playing == "y":

    player_hand = []
    dealer_hand = []

    keep_drawing = True
    player_lost = False
    dealer_lost = False

    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

    if sum(player_hand) == 21 and sum(dealer_hand) != 21:
        print(f"Dealer hand {dealer_hand}. Your hand: {player_hand}")
        print("You have BlackJack! You have won! :3")
        keep_drawing = False
        player_lost = True

    elif sum(player_hand) == 21 and sum(dealer_hand) == 21:
        print(f"Dealer hand {dealer_hand}. Your hand: {player_hand}")
        print("There is a draw!")
        keep_drawing = False
        player_lost = True

    while keep_drawing:
        print(f"Dealers hand: [{dealer_hand[0]}, *]. Dealer has {sum(dealer_hand)}.")
        print(f"Your hand: {player_hand}. You have {sum(player_hand)}.")

        draw_a_card = input("Do you want to draw another card? Type 'y' or 'n': ").lower()

        if draw_a_card == "y":
            player_hand.append(random.choice(cards))
            
            if sum(player_hand) > 21 and player_hand.count(11) != 0:
                print(f"Your hand: {player_hand}")
                player_hand[player_hand.index(11)] = 1
                print(f"You have {sum(player_hand)}.")

            elif sum(player_hand) > 21:
                print(f"Your hand: {player_hand}")
                print(f"You have {sum(player_hand)}, you have boosted.")
                keep_drawing = False
                player_lost = True

        else:
            keep_drawing = False
            print(f"Dealer hand: {dealer_hand}")
            
            keep_drawing_dealer = True
            while sum(dealer_hand) < 17 and keep_drawing_dealer:
                dealer_hand.append(random.choice(cards))
                if sum(dealer_hand) > 21:
                    keep_drawing_dealer = False
                    dealer_lost = True
                    
                if dealer_lost:
                    print(f"Dealer hand: {dealer_hand}")
                    print("Dealer has busted, you win!")
                else:
                    print(f"Dealer hand: {dealer_hand}")
                
    if not player_lost and not dealer_lost:
        if sum(dealer_hand) > sum(player_hand):
            print(f"Dealer has {sum(dealer_hand)}, you have {sum(player_hand)}. Dealer wins!")

        elif sum(dealer_hand) == sum(player_hand):
            print(f"Dealer has {sum(dealer_hand)}, you have {sum(player_hand)}. Draw!")

        elif sum(dealer_hand) < sum(player_hand):
            print(f"Dealer has {sum(dealer_hand)}, you have {sum(player_hand)}. You win!")

    keep_playing = input("Do you want to start another game? Type 'y' or 'n': ").lower()      

print("We really wish you a happy and funny day!:)") 
