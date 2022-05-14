"""Component 4 (Random Generator) -- Function -- Version 2
Converting 06_v6 into a recyclable function so I able to use any list
of words for my code
I now am able to swap the language and questions around for easy and hard mode
Written by Katelyn Gee
Created 10/05/2022"""

import random


def random_generator(lists, asking, num1, num2, num3):

    # Variables
    score = 0

    # Plays 5 rounds
    for i in range(10):

        # Mixes up the list so different question is chosen
        random.shuffle(lists)

        # Asks the user the question
        question = input(asking.format(lists[0][num2])).title()

        # if user got it right
        if question == lists[0][num1] or question == lists[0][num3]:
            answer = "right! Congratulations!"
            score += 1

        # if user got it wrong
        else:
            answer = f"wrong, the correct answer was '{lists[0][num1]}'. Try again next time! "

        # printing if user was right or wrong
        print(f"You got it {answer}")
        print()

        # To avoid questions being repeated, each question is removed once displayed
        lists.pop(0)


# List of English and Maori numbers
numbers = [["1", "One", "Tahi"],
           ["2", "Two", "Rua"],
           ["3", "Three", "Toru"],
           ["4", "Four", "Wha"],
           ["5", "Five", "Rima"],
           ["6", "Six", "Ono"],
           ["7", "Seven", "Whitu"],
           ["8", "Eight", "Waru"],
           ["9", "Nine", "Iwa"],
           ["10", "Ten", "Tekau"]]

# To test if it is working for English and Maori words in the same code
numbers_2 = numbers.copy()

# Calling on function for English
print("English round \n")
random_generator(numbers, "What is {} in Maori? ", 2, 0, 0)

# Calling on function for Maori
print("Maori round \n")
random_generator(numbers_2, "What is {} in Englsih? ", 0, 2, 1)
