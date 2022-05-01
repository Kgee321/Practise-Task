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


def winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        win = "no one"
        return win
    if computer_choice == "Rock" and user_choice  == "Paper" or \
            computer_choice == "Paper" and user_choice  == "Scissors" or \
            computer_choice == "Scissors" and user_choice  == "Rock":
        win = "winner"
        return win

    else:
        win = "losser"
        return win


# Asking for username
name = input("What is your name? ").title()

# Calling on yes_no function
instructions = checker(f"Do you know how to play Paper Scissors Rock {name}? Yes/No ", "yes", "no", "yes")

# display instructions by calling game_rule functions
if instructions == "No":
    game_rules()

# print winner of each round
rounds = 1
user_score = 0
computer_score = 0

while rounds < 4:

    # number of rounds
    print("---------------------------------------")
    print(f"Round {rounds}")

    # Player chooses an element
    user = checker("Choice either Paper (P), Scissors (S) or Rock (R): ", "rock", "paper", "scissors")

    # Computer choosing random element
    computer = random_choice("RPS", "Rock", "Paper", "Scissors")
    print(f"Computer did {computer}")
    print()

    # Winner decided
    scoring = winner(computer, user)

    # user won
    if scoring == "winner":
        print(f"Congratulations! You Won round {rounds}!")
        user_score += 1
        rounds += 1

    # computer won
    if scoring == "losser":
        print(f"Better Luck Next time! You lost round {rounds}.")
        computer_score += 1
        rounds += 1

    # It was a draw
    if scoring == "no one":
        print("It was a draw, try again")
    print()

    # Checking if it is the final round
    if rounds == 4:
        print("The Final Score is: ")
    else:
        print("The score is:")

    # printing out the score each round

    print(f"{user_score} to you and {computer_score} to the computer")

# Winner of all the rounds
print()
if user_score == computer_score:
    print("It was a draw! Play again to determine a winner")
if user_score > computer_score:
    print("YOU WON!! Congratulation!!")
else:
    print("You lost! Try again next time")
