# create the coffe machine class

class CoffeeMachine:

    def __init__(self):
        self.water= 300
        self.milk= 200
        self.coffee= 100
        self.money= 0

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}gr")
        print(f"Money: ${self.money}")

    def resources_checker(self, flavours, coffee_flavour):
        """Take a flavour and check if the machine has enough resources to prepare the coffee"""
        required_resources = flavours[coffee_flavour]

        for resource in required_resources:
            if resource != "price":
                if getattr(self, resource, 0) < required_resources[resource]:
                    print(f"There is no sufficient {resource}.")
                    return False
                else:
                    return True

    def update_machine(self, flavours, coffee_flavour):
        for key, value in flavours[coffee_flavour].items():
            current_value = getattr(self, key, 0)
            if key == "price":
                setattr(self, key, current_value + value)
            else:
                current_value = getattr(self, key)
                setattr(self, key, current_value - value)