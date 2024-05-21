print("Welcome to the tip calculator!")

bill = int(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give?: 10, 12 or 15? "))
while tip not in [10,12,15]:
    tip = int(input("Please enter a valid tip amount: 10, 12 or 15 "))
people = int(input("How many ways would you like to split the bill?: "))
total =bill * (1 + (tip / float(100)))



print(f"The total bill is ${total:.2f} and each person should pay ${(total / people):.2f}.")
