"""Final code -- I put together my separate codes parts to make my final code
My final code should ask user for name, get the user and computer to choice either paper, scissors or rock, and print the winner after 3 rounds
Written by Katelyn Gee
On 20th of March, Sunday, 2022
"""

import random


def main_function(the_round, p_s, t_s):
    # tells player what round it is
    checker = p_s + t_s
    if checker < 3:
        print("--" * 50)
        print(f"Round {the_round}")
        print()
    while the_round <= 3:

        # Asks for user input
        element = input("Enter either P for Paper, S for Scissors and R for Rock: ").upper()

        # Computer choices a random element
        computer = random.choice("RPS")
        if computer == "R":
            computer_choice = "Rock"
        elif computer == "P":
            computer_choice = "Paper"
        elif computer == "S":
            computer_choice = "Scissors"

        print(f"Computer chose {computer_choice}")

        if element == "P" or element == "R" or element == "S":
            # Calls on the function which prints the winner of that round
            winner(the_round, computer, element, p_s, t_s)

        else:
            # Checking for correct letter inputted
            print("That was not a correct input: Try again")
            main_function(the_round, p_s, t_s)


def winner(number, comp, letter, player_score, comp_score):
    if letter == comp:
        # Checking if there is a draw
        print("It was a draw: Try again")
        main_function(number, player_score, comp_score)

    elif comp == "R" and letter == "P" or \
            comp == "P" and letter == "S" or \
            comp == "S" and letter == "R":
        # Checking to see if user beat the computer
        print(f"Congratulations {name}, you won round {number}")
        player_score += 1
        number += 1

    else:
        # If the user did not beat the computer
        print(f"I am sorry {name}, you lost round {number}")
        comp_score += 1
        number += 1
    print()
    # prints out computer score and user score
    print(f"The score is now {player_score} to you and {comp_score} to the computer")
    main_function(number, player_score, comp_score)


def end_screen(user_score, code_score):
    print()
    print("__"*50)
    print()
    if user_score < code_score:
        print(f"Sorry {name}, you lost. Restart to try again")
    if user_score > code_score:
        print(f"Good Job {name}! You Won. Restart to play again")
    else:
        print(f"{name}, you tied with the computer. Restart to try again")


# Welcoming user
print("--------- Paper Scissors Rock ------------")
name = input("Enter your name: ")
print(f"Welcome {name}!")

# Starting values
rounds = 1
person_score = 0
tech_score = 0

# Calling main function
main_function(rounds, person_score, tech_score)
