"""Winner component -- version 1
Adding in the winner or loser elements to determined who loses or wins the round
Also adding score
Putting it all in a function so it is easy to test"""


def winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        win = "No one"
        return win
    if computer_choice == "Rock" and user_choice  == "Paper" or \
            computer_choice == "Paper" and user_choice  == "Scissors" or \
            computer_choice == "Scissors" and user_choice  == "Rock":
        win = "winner"
        return win

    else:
        win = "losser"
        return win


# Main function called
print(winner("Rock", "Paper"))
print(winner("Paper", "Rock"))
print(winner("Rock", "Scissors"))
print(winner("Scissors", "Scissors"))
