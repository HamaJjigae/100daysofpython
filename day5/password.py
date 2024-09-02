import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
num_letters = 0
num_numbers = 0
num_symbols = 0
while True:
    try:
        while num_letters <= 0:
            num_letters = int(input("Please enter the number of letters you want in your password: "))
        break
    except ValueError:
        print("Please enter a number")
while True:
    try:
        while num_numbers <= 0:
            num_numbers = int(input("Please enter the number of numbers you want in your password: "))
        break
    except ValueError:
        print("Please enter a number")
while True:
    try:
        while num_symbols <= 0:
            num_symbols = int(input("Please enter the number of symbols you want in your password: "))
        break
    except ValueError:
        print("Please enter a number")

password_characters = (
        [random.choice(letters) for _ in range(num_letters)] +
        [random.choice(numbers) for _ in range(num_numbers)] +
        [random.choice(symbols) for _ in range(num_symbols)]
        )

random.shuffle(password_characters)
password = ''.join(password_characters)

print(f" Password: {password}")
