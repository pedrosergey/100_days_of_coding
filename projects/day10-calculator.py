# import the main logo and the os libraty to use the clear function

from ascii_images import day10_logo
import os

# create the different operations 

def sum(num1, num2):
    return (num1 + num2)

def subtract(num1, num2):
    return (num1 - num2)

def multiply(num1, num2):
    return (num1 * num2)

def divide(num1, num2):
    return (num1 / num2)

# create the dictionary to save the operations

operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(day10_logo)
print("Welcome to the magic calculator!!")

machine_status = True

while machine_status:
    n1 = float(input("Please, introduce a number: "))
    continue_calculating = True

    for operation in operations:
        print(operation)

    while continue_calculating:

        operation = input("Which operation do you want to perform?: ")
        n2 = float(input("Please, introduce the other number: "))

        n1 = operations[operation](n1, n2)

        print(f"The result is {n1:.2f}")

        want_continue = input("Do you want to continue calculating with the same number? Type 'y' or 'n': ").lower()
        
        if want_continue != "y":
            continue_calculating = False
            turn_off_machine = input("Do you want to perform another operation? Type 'y' or 'n': ").lower()

            if turn_off_machine == 'y':
                os.system("clear")
            else:
                machine_status = False

print("Thanks for using our brand new system of calculus!")





