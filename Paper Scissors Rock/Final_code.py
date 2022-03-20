"""Final code -- I put together my seperate codes parts to make my final code
My final code should ask user for name, get the user and computer to choice either paper, scissors or rock, and print the winner after 3 rounds
Written by Katelyn Gee
On 20th of March, Sunday, 2022
"""


import random


def main_function(round, player, p_s, t_s):

    # tells player what round it is
    print("--" * 50)
    print()
    print(f"Round {round}")
    while round <= 3:

        # Asks for user input
        element = input("Enter either P for Paper, S for Scissors and R for Rock: ").upper()

        # Computer choices a random element
        computer = random.choice("RPS")
        print(f"Computer chose {computer}")

        if element == "P" or element == "R" or element == "S":
            # Calls on the function which prints the winner of that round
            winner(round, computer, element, p_s, player, t_s)

        if element == computer:
            # Checking if there is a draw
            print("It was a draw: Try again")
            main_function(round, player, p_s, t_s)

        else:
            # Checking for correct letter inputted
            print("That was not a correct input: Try again")
            main_function(round, player, p_s, t_s)

    end_screen(player, p_s, t_s)


def winner(number, comp, letter, player_score, name, comp_score):
    if comp == "R" and letter == "P" or \
            comp == "P" and letter == "S" or \
            comp == "S" and letter == "R":
        print(f"Congratulations {name}, you won round {number}")
        player_score += 1
        number += 1
    else:
        print(f"I am sorry {name}, you lost round {number}")
        comp_score += 1
        number += 1
    print()
    print(f"The score is now {player_score} to you and {comp_score} to the computer")
    main_function(number, letter, player_score, comp_score)


def end_screen(person, user_score, code_score):
    if user_score < code_score:
        print(f"Sorry {person}, you lost. Restart to try again")
    if user_score > code_score:
        print(f"Good Job {person}! You Won. Restart to play again")
    else:
        print(f"{person}, you tied with the computer. Restart to try again")


# Welcoming user
print("--------- Paper Scissors Rock ------------")
name = input("Enter your name: ")
print(f"Welcome {name}!")

# Starting values
rounds = 1
person_score = 0
tech_score = 0

# Calling main function
main_function(rounds, name, person_score, tech_score)
