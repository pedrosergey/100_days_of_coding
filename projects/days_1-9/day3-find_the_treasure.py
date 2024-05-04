from data.ascii_images import day3_logo

print(day3_logo)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_answer = input("You are in a cross-road, and you need to choose 'left' or 'right' to keep your path. Which direction will you take? ")

if first_answer == "left":
  print("You are eaten by crocodiles")
elif first_answer == "right":
  second_answer = input("You arrive to a river, will you 'take' the boat, or will you 'swim'? ")
  if second_answer == "swim":
    third_answer = input("After crossing the river, you see three doors. Do you choose the 'red', the 'blue' or the 'green' door? ")
    if third_answer == "red":
      print("You are burned!")
    elif third_answer == "blue":
      print('You are eated by a lion!')
    elif third_answer == "green":
      print("You find the treasure!!")
  if second_answer == "take":
    print("Some local indians kill you with arrows")