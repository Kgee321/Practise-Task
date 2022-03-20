"""Creating the main function -- To welcome user too game, ask their name and what element they are choosing
Also calls on random and makes the computer randomly choose an element
Katelyn Gee
19/03/2022"""

import random


def main_function():
    element = input("Enter either P for Paper, S for Scissors and R for Rock: ").upper()
    computer = random.choice("RPS")
    if element != "P" or element != "R" or element != "S":
        print("That was not a correct input: Try again")
        main_function()
    if element == computer:
        print(f"You choice {element} and computer choice {computer}. It was a draw: Try again")
        main_function()
    else:
        winner()


print("--------- Paper Scissors Rock ------------")
name = input("Enter your name: ")
main_function()
