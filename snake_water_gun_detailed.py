import random

'''
1 for snake
2 for water
3 for gun
'''

computer = random.choice([1, 2, 3])
you = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

youDict = {"s": 1, "w": 2, "g": 3}
reverseDict = {1: "snake", 2: "water", 3: "gun"}

if you not in youDict:
    print("Invalid input! Please choose s, w, or g.")
else:
    younum = youDict[you]
    print(f"You chose {reverseDict[younum]} and computer chose {reverseDict[computer]}")

    if computer == younum:
        print("It's a draw")
    else:
        if (computer == 1 and younum == 2) or \
           (computer == 2 and younum == 3) or \
           (computer == 3 and younum == 1):
            print("You win")
        else:
            print("You lose")
# Detailed implementation of Snake–Water–Gun game
# Focuses on clarity and explicit logic
