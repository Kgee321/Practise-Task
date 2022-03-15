"""Main function -- Welcomes the user and asks them to input the activity they are doing
Katelyn Gee
16/03/2022
"""


def main_function():
    print()

    # Starting variables
    kidz_total_age = 0
    kidz_total_people = 0
    fun_total_age = 0
    fun_total_people = 0

    # Choosing a holiday program
    program = input("Either enter a Holiday Program -- Fun in the Sun (F) or Active Kidz (A)"
                    "or end code -- enter X:"
                    "").upper()

    # Entering age of child
    valid = False
    while not valid:
        try:
            years = int(input("What is the child's age in year: "))
            valid = True
        except ValueError:
            print("Please choice a whole number (integer)")

    if program == "A":
        kidz_total_age += years
        kidz_total_people += 1
        main_function()
    elif program == "F":
        fun_total_age += years
        fun_total_people +=
        main_function()
    elif program == "X":
        end_screen(kidz_total_age, kidz_total_people,fun_total_age,fun_total_people,)








print(f"{'--'*20}Welcome to Kidz Fun Holiday Programs{'--'*20}")
main_function()
