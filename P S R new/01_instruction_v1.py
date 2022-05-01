"""Instructions component -- Version 1
Ask for name
Start of yes and no checker where user can only enter Yes or No"""

# Asking for username
name = input("What is your name? ")
print(f"Hello {name}")

# Ask if user knows how to play
instruction = input("Do you know how to play Paper Scissors Rock? Yes/No ")

# Yes is entered, program continues
if instruction == "Yes":
    print("Program continues")

# No is entered, instructions displayed
elif instruction == "No":
    print("Instructions displayed")

else:
    print("Incorrect input")
