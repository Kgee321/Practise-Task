""" Calling main_function -- Welcoming the user to DugRus
Created by Katelyn Gee
14/03/2022
"""


def main_function():
    ask = input("""What do you want to do:
D for drop off a dog
P for Pick up a dog
L for a list of all the dogs staying
C for the amount of charge for the stay
E for exit program.
""").upper
    while ask != "E":
        if ask == DROP_OFF:
            drop_off()
        elif ask == PICK_UP:
            pick_up()
        elif ask == LIST_OF_DOGS:
            list_of_dogs()
        elif ask == CHARGE_OF_STAY:
            charge_of_stage()
    end_of_program()


# Permanent variables
DROP_OFF = "D"
PICK_UP = "P"
LIST_OF_DOGS = "L"
CHARGE_OF_STAY = "C"

# Calling main function
print(f"{'--' * 10} Welcome to DogRus: a boarding house for dogs{'--' * 10}")
main_function()
