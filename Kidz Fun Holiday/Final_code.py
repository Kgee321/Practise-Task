"""Final code -- Putting all my separate codes together to make the overall code
Katelyn Gee
16/03/2022
Editing mistakes: 17/03/2022
"""


def main_function(kidz_a, kidz_p, fun_a, fun_p):
    print()

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
                if years < 16:
                    valid = True
                else:
                    print("Children must be under 16 years of age: Try again")
            except ValueError:
                print("Please choice a whole number (integer): Try again")

        if program == "A":
            kidz_a += years
            kidz_p += 1
            print("\nChild been added to Active Kidz Program")
            main_function(kidz_a, kidz_p, fun_a, fun_p)
        elif program == "F":
            fun_a += years
            fun_p += 1
            print("\nChild been added to Fun in the Sun Program")
            main_function(kidz_a, kidz_p, fun_a, fun_p)
    elif program == "X":
        end_screen(kidz_a, kidz_p, fun_a, fun_p)
    else:
        print("Incorrect input: Try again")
        main_function(kidz_a, kidz_p, fun_a, fun_p)


def end_screen(kidz_age, kidz_people, fun_age, fun_people):
    print()
    print(f"Here is the average age and total child in the holiday program:"
          f"\nTotal children in Active Kidz: {kidz_people}"
          f"\nAverage Active Kidz age: {kidz_age/kidz_people:.0f}"
          f"\nTotal children in Fun in the Sun: {fun_people}"
          f"\nAverage Fun in the Sun age: {fun_age/fun_people:.0f}")


# starting variables
kidz_total_age = 0
kidz_total_people = 0
fun_total_age = 0
fun_total_people = 0

print(f"{'--'*20}Welcome to Kidz Fun Holiday Programs for under 16's{'--'*20}")
main_function(kidz_total_age, kidz_total_people, fun_total_age, fun_total_people)
