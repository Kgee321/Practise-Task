"""Winner component -- version 1
Determines if the user and computer drawed
if no, program continues
Using a test element for the time being"""

# Element choice for testing (delete later)
computer_choice = "Rock"
user_choice = "Rock"

# Checking if it was a draw
if computer_choice == user_choice:
    print("Draw, try again")
else:
    print("Program continues")
