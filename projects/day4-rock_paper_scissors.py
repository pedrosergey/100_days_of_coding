from project_data.ascii_images import rock, paper, scissors
import random

computer_choice = random.randint(0,2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n")) 

options = [rock, paper, scissors]

print(options[player_choice])

print("The computer choice: \n", options[computer_choice])

if player_choice == computer_choice:
  print("You draw")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
  print("You win!")
else:
  print("You lost!")
