"""Instructions component -- Version 3
Converting Version 2 into a reusable functions
 Creating a new functions to print game rules
 """


def yes_no(question):
    while True:
        # Ask if user knows how to play
        instruction = input(question).lower()

        # Yes is entered, program continues
        if instruction == "yes" or instruction == "y":
            checker = "Yes"
            return checker

        # No is entered, instructions displayed
        elif instruction == "no" or instruction == "n":
            checker = "No"
            return checker

        else:
            print("Incorrect input, make sure you enter Yes/No")
    return checker


def game_rules():
    print("*** How To Play ***")
    print()
    print("Instructions displayed")
    print()
    print("program continues")


# Asking for username
name = input("What is your name? ").title()

# Calling on yes_no function
instructions = yes_no(f"Do you know how to play Paper Scissors Rock {name}? Yes/No ",)

# display instructions by calling game_rule functions
if instructions == "No":
    game_rules()

