import random
rps_list = ["Rock","Paper","Scissors"]
user_input = 0
while True:
        try:
                user_input = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
                if user_input in [0,1,2]:
                        break
                else:
                        print("Invalid input. Please enter 0, 1 or 2")
        except ValueError:
                print("Invalid input. Please enter a number.")
random_input = random.randint(0,2)

if user_input == random_input:
        print(f"{rps_list[user_input]} vs {rps_list[random_input]} is a draw!")
elif (user_input == 0 and random_input == 2) or \
        (user_input == 1 and random_input == 0) or \
        (user_input == 2 and random_input == 1):
        print(f"{rps_list[user_input]} vs {rps_list[random_input]} is a Win!")
else:
        print(f"{rps_list[user_input]} vs {rps_list[random_input]} is a Loss!")

