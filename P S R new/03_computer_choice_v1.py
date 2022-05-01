"""Component computer choice -- version 1
Getting the computer to choose a random element
of paper or scissors or rock
Katelyn Gee
1/05/2022"""

import random

# computer chooses random letter
computer = random.choice("RPS")

# print full name from letters
if computer == "R":
    computer_choice = "Rock"
    print(computer_choice)
elif computer == "P":
    computer_choice = "Paper"
    print(computer_choice)
elif computer == "S":
    computer_choice = "Scissors"
    print(computer_choice)
