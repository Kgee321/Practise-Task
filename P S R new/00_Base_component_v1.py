"""All the functions and game parts combined
I add the functions to this code as I create them
Katelyn Gee
1/05/2022
 """

import random


def checker(question, answer_one, answer_two, answer_three):
    while True:
        # Ask if user knows how to play
        instruction = input(question).lower()

        # Yes is entered, program continues
        if instruction == answer_one or instruction == answer_one[0]:
            answer = answer_one.title()
            return answer

        # No is entered, instructions displayed
        elif instruction == answer_two or instruction == answer_two[0]:
            answer = answer_two.title()
            return answer

        elif instruction == answer_three or instruction == answer_three[0]:
            answer = answer_three.title()
            return answer

        else:
            print("Incorrect input, make sure you enter Yes/No")


def game_rules():
    print("*** How To Play ***")
    print()
    print("Instructions displayed")
    print()
    print("program continues")


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


# Asking for username
name = input("What is your name? ").title()

# Calling on yes_no function
instructions = checker(f"Do you know how to play Paper Scissors Rock {name}? Yes/No ", "yes", "no", "yes")

# display instructions by calling game_rule functions
if instructions == "No":
    game_rules()

# Player chooses an element
user = checker("Choice either Paper (P), Scissors (S) or Rock (R): ", "rock", "paper", "scissors")


# Computer choosing random element
computer = random_choice("RPS", "Rock", "Paper", "Scissors")

