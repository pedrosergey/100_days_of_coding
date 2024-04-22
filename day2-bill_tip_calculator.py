print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $ "))

tip_percentage = int(input("How much tip percent would like to give? 10, 12 or 15? "))

people_paying = int(input("How manu people to split the bill? "))

bill_with_tip = total_bill * (1+tip_percentage/100)

bill_per_person = round(bill_with_tip / people_paying, 2)

print(f"Each person should pay ${bill_per_person:.2f}.")