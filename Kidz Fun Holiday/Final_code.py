"""Final code -- Putting all my sepreate codes toegther to make the overall code
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
                    " \nor end code -- enter X:"
                    "\n").upper()
    if program == "A" or program == "F":

        # Entering age of child
        valid = False
        while not valid:
            try:
                years = int(input("Enter the child's age in year: "))
                valid = True
            except ValueError:
                print("Please choice a whole number (integer)")

        if program == "A":
            kidz_total_age += years
            kidz_total_people += 1
            print("\nChild been added to Active Kidz Program")
            main_function()
        elif program == "F":
            fun_total_age += years
            fun_total_people += 1
            print("\nChild been added to Fun in the Sun Program")
            main_function()
    elif program == "X":
        end_screen(kidz_total_age, kidz_total_people,fun_total_age,fun_total_people,)
    else:
        print("Incorrect input: Try again")
        main_function()


def end_screen(kidz_age, kidz_people, fun_age, fun_people):
    print()
    print(f"Here is the average age and total child in the holiday program:"
          f"\nTotal children in Active Kidz: {kidz_people}"
          f"\nAverage Active Kidz age: {kidz_age/kidz_people}"
          f"\nTotal children in Fun in the Sun: {fun_people}"
          f"\nAverage Fun in the Sun age: {fun_age/fun_people}")






print(f"{'--'*20}Welcome to Kidz Fun Holiday Programs{'--'*20}")
main_function()
