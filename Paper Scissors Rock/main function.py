"""Creating the main function -- To welcome user too game, ask their name and what element they are choosing
Also calls on random and makes the computer randomly choose an element
End screen function prints off who won the game whether it was the user or the computer
Katelyn Gee
19/03/2022
Edited on 20/03/2022"""

import random


def main_function(round, player, p_s, t_s):

    # tells player what round it is
    round += 1
    print(f"Round {round}")
    while round <= 3:

        # Asks for user input
        element = input("Enter either P for Paper, S for Scissors and R for Rock: ").upper()

        # Computer choices a random element
        computer = random.choice("RPS")
        print(f"Computer chose {computer}")

        if element != "P" or element != "R" or element != "S":
            # Checking for correct letter inputted
            print("That was not a correct input: Try again")
            main_function()
        if element == computer:
            # Checking if there is a draw
            print("It was a draw: Try again")
            main_function()
        else:
            # Calls on the function which prints the winner of that round
            winner(round, computer, element, p_s, player, t_s)
    end_screen(player, p_s, t_s)


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
print(f"Welcome {name}:")

# Starting values
rounds = 0
person_score = 0
tech_score = 0

# Calling main function
main_function(rounds, name, person_score, tech_score)
