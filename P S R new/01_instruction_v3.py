"""Instructions component -- Version 3
Converting Version 2 into a loop so it can easily be tested """


loop = ""
while loop != "x":
    # Asking for username
    name = input("What is your name? ").title()
    print(f"Hello {name}")

    # Ask if user knows how to play
    instruction = input(f"Do you know how to play Paper Scissors Rock {name}? Yes/No ").lower()

    # Yes is entered, program continues
    if instruction == "yes" or instruction == "y":
        print("Program continues")

    # No is entered, instructions displayed
    elif instruction == "no" or instruction == "n":
        print("Instructions displayed")

    else:
        print("Incorrect input")
    print()

