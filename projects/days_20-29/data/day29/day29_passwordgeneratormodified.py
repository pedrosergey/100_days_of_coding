import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class Password:
    def __init__(self):
        self.nr_letters = 12
        self.nr_symbols = 4
        self.nr_numbers = 4
        self.password = []
        self.string_password = ''

        for letter in range(1, self.nr_letters + 1):
            self.password.append(random.choice(letters))

        for symbol in range(1, self.nr_symbols + 1):
            self.password.append(random.choice(symbols))

        for number in range(1, self.nr_numbers + 1):
            self.password.append(random.choice(numbers))

        random.shuffle(self.password)

        for char in range(0, len(self.password)):
            self.string_password += self.password[char]
