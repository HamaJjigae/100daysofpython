import random
friends = ["Alice", "Bob", "Charlie", "David", "Ethan"]

random_name = random.randint(0,(len(friends)-1))
print(friends[random_name])

print(random.choice(friends))