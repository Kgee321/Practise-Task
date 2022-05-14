import random

numbers = [["1", "tahi"],
           ["2", "rua"],
           ["3", "toru"],
           ["4", "wha"],
           ["5", "rima"],
           ["6", "ono"],
           ["7", "whitu"],
           ["8", "waru"],
           ["9", "iwa"],
           ["10", "tekau"]]

random.shuffle(numbers)

print(numbers)

question = input("What is the {} in english ".format(numbers[0][1]))

if question == numbers[0][0]:
    print("WORKKING")
else:
    print("Oof")
