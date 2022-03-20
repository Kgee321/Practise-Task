"""Winner function -- Will print out the winner of the match.
It is normal paper scissors rock with rock beating scissors, scissors beating paper and paper beating rock.
Written by Katelyn Gee
On the 20th of March, Sunday, 2022
"""


def winner(number, comp, letter, player_score, name, comp_score):
    if comp == "R" and letter == "P" or \
            comp == "P" and letter == "S" or \
            comp == "S" and letter == "R":
        print(f"Congratulations {name}, you won round {number}")
        player_score += 1
    else:
        print(f"I am sorry {name}, you lost round {number}")
        comp_score += 1
    print(f"The score is now {player_score} to you and {comp_score} to the computer")
    main_function(number, letter, player_score, comp_score)
