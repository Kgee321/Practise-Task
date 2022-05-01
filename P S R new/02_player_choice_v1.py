"""player choice component -- Version 1
Trialing to see if I can convert the yes/no checker to be able to be used
for player choosing paper or scissors or rock.
It works!
 """


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


# Asking for username
name = input("What is your name? ").title()

# Calling on yes_no function
instructions = checker(f"Do you know how to play Paper Scissors Rock {name}? Yes/No ", "yes", "no", "yes")
print(instructions)

# Player chooses an element
choice = checker("Choice either Paper (P), Scissors (S) or Rock (R): ", "rock", "paper", "scissors")
print(choice)

# display instructions by calling game_rule functions
# if instructions == "No":
#   game_rules()
