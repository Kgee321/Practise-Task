""" Calling main_function -- Welcoming the user to DugRus
Created by Katelyn Gee
14/03/2022
"""


def main_function():
    print()
    ask = input("""What do you want to do:
D for drop off a dog
P for Pick up a dog
L for a list of all the dogs staying
C for the amount of charge for the stay
E for exit program.
""").upper
    while ask != CANCEL:
        if ask == DROP_OFF:
            drop_off(all_dogs)
        elif ask == PICK_UP:
            pick_up(all_dogs)
        elif ask == LIST_OF_DOGS:
            list_of_dogs(all_dogs)
        elif ask == CHARGE_OF_STAY:
            calc_cost(len(all_dogs))
        else:
            print("""You must enter either:
D for Drop off
P for Pick up
L for list of all dogs
C for the cost of staying or
E for exit program""")
            print()
            main_function()
    exit_program()


# Permanent variables
DROP_OFF = "D"
PICK_UP = "P"
LIST_OF_DOGS = "L"
CHARGE_OF_STAY = "C"
CANCEL = "E"
COST_PER_DAY = 22.50

# Calling main function
print(f"{'--' * 10} Welcome to DogRus: a boarding house for dogs{'--' * 10}")
all_dogs = []
main_function()
