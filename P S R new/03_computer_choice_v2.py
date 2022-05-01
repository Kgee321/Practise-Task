"""Component computer choice -- version 1
Converting version 1 into a function so that in the future my code will
be easy to change
Katelyn Gee
1/05/2022"""

import random


def random_choice(letters, option_one, option_two, option_three):

    # computer chooses random letter
    computer = random.choice(letters)

    # print full name from letters
    if computer == letters[0]:
        computer_choice = option_one
        return computer_choice
    elif computer == letters[1]:
        computer_choice = option_two
        return computer_choice
    elif computer == letters[2]:
        computer_choice = option_three
        return computer_choice


print(random_choice("RPS", "Rock", "Paper", "Scissors"))
