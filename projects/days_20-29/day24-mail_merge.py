# read the names of the people to send the letters

with open("data/day24/Input/Names/invited_names.txt") as n:
    names_list = n.readlines()

# read the template letter

with open("data/day24/Input/Letters/starting_letter.txt") as l:
    letter = l.read()

# create the letters for all names

for name in names_list:
    name = name.strip()
    with open(f"data/day24/Output/ReadyToSend/letter_{name}.txt", mode='w') as l:
        l.write(letter.replace('[name]', name))
