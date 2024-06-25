import sys
print("""
        /\\____;;___\\
       | /         /
       `. ())oo() .
        |\\(%()*^^()^\\
       %| |-%-------|
      % \\ | %  ))   |
      %  \\|%________|
       %%%%
""")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("\n\nYou pull up to a fork in the road, on the left is a narrow passageway; the right, a bumpy path.")
choice = input("Do you go \'Left\' or \'Right\'?  ")
if choice != 'Left':
    print("Oh no! You fell into a hole! GG")
    sys.exit()

print("\n\nYou get to a river crossing, but there are alligators swimming in the water.")
choice = input("Do you \'Swim\' or \'Wait\'?  ")

if choice != 'Wait':
    print("Wow who could have guessed that the alligators would get you. GG")
    sys.exit()

print("\n\nSuddenly three doors appear in front of you: a red door radiating heat, a blue door with loud noises behind it, or a yellow door with mysterious whispers eminating from the handle.")
choice = input("Do you choose: \'Red\', \'Blue\' or \'Yellow\'?  ")

if choice == "Red":
    print("Fire explodes from the open door and you die. GG")
elif choice == "Blue":
    print("Vicious beasts pour out and eat you alive. GG")
elif choice == "Yellow":
    print("The whispers were just wind passing through the keyhole, you escape!")
else:
    print("Invalid input. Guess you can't even type properly. GG")
