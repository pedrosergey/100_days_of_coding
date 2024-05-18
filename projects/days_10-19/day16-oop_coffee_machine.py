# import some libraries

from data.day16_coffeeclass import CoffeeMachine

# especify the flavours and the required resources

flavours = {
    "espresso": {"price": 1.5, "water": 50, "coffee": 18},
    "latte": {"price": 2.5, "water": 200, "coffee": 24, "milk": 150},
    "capuccino": {"price": 3.0, "water": 250, "coffee": 24, "milk": 100},
}

possible_coins = [1, 5, 10, 25]


# create a function that will check how much money does the user inputs the machine

def insert_coins():
    """Ask how many coins will they insert into the machine"""
    print("Please, insert the coins.")
    coins = ["quarters", "dimes", "nickles", "pennies"]
    values = [0.25, 0.10, 0.05, 0.01]
    number_of_coins = []
    total_value = 0

    for coin in coins:
        number_of_coins.append(int(input(f"How many {coin}?: ")))

    for coin_value in range(0, len(coins)):
        total_value += values[coin_value] * number_of_coins[coin_value]

    return total_value


# create the coffe machine

coffee_machine = CoffeeMachine()


# create the final function that will prepare the coffee

def make_coffe():
    chosen_flavour = input("What would you like? Espresso, latte or capuccino?: ").lower()
    options = ["espresso", "latte", "capuccino", "report"]

    if chosen_flavour == "report":
        coffee_machine.report()
        return True
    elif chosen_flavour == "off":
        print("Have a great day ahead 🌻! :)")
        return False
    else:
        while chosen_flavour not in options:
            chosen_flavour = input("Please, enter a valid answer. Espresso, latte or capuccino?: ").lower()

        if not coffee_machine.resources_checker(flavours=flavours, coffee_flavour= chosen_flavour):
            print("Sorry, there are not sufficient resources to make your coffee.")
            return True

        else:

            inserted_coins = insert_coins()
            coffee_price = flavours[chosen_flavour]["price"]

            if inserted_coins < coffee_price:
                print(f"Sorry, that is not enough money. ${inserted_coins} refunded.")
                return True
            else:
                if inserted_coins == coffee_price:
                    print("You introduced the exact amount. No change for you!")
                else:
                    print(f"${round(inserted_coins - coffee_price, 2)} were give back to you.")

                coffee_machine.update_machine(flavours=flavours, coffee_flavour=chosen_flavour)
                print(f"Here you have your {chosen_flavour}. Enjoy it! ☕")
                return True

machine_status = True

while machine_status:
    machine_status = make_coffe()
