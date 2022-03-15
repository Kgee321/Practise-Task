"""End_screen function -- on user command, takes them to the home screen with the average
age and number of people in each holiday program
Katelyn Gee
16/03/2022
"""


def end_screen(kidz_age, kidz_people, fun_age, fun_people):
    print()
    print(f"Here is the average age and total child in the holiday program:"
          f"Total children in Active Kidz: {kidz_people}"
          f"Average Active Kidz age: {kidz_age/kidz_people}"
          f"Total children in Fun in the Sun: {fun_people}"
          f"Average Fun in the Sun age: {fun_age/fun_people}")
