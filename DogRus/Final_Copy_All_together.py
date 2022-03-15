"""Final Copy -- Combining all the functions and different codes I made to make the final code
Katelyn Gee
15/03/2022
"""


def main_function():
    # permanent variables
    drop = "D"
    pick = "P"
    roll_of_dogs = "L"  # I am unsure why it does not what to be capitalised. Can you help me?
    charge = "C"
    cancel = "E"

    # Main code
    print()
    ask = input("""What do you want to do:
D for drop off a dog
P for Pick up a dog
L for a list of all the dogs staying
C for the amount of charge for the stay
E for exit program.
""").upper()

    # call a function depending on what letter inputted
    if ask == drop:
        drop_off()
    elif ask == pick:
        pick_up()
    elif ask == roll_of_dogs:
        list_of_dogs()
    elif ask == charge:
        calc_cost(len(roll))
    elif ask == cancel:
        exit_program()
    else:
        # if an incorrect letter is inputted, restart.
        print("""That is an incorrect value, try again""")
        print()
        main_function()


def drop_off():
    name = input("Enter the name of the dog being dropping off: ").lower()
    print()

    # adding requested dog to the roll
    roll.append(name.title())
    print(f"{name.title()} has been dropped off")
    main_function()


def pick_up():
    name = input("Enter the name of the dog being picked up: ").title()

    # checking to see if dog requested is in the roll.
    if name in roll:
        roll.remove(name)
        print(f"{name} has been removed from the roll")
        main_function()
    else:
        print("There is no dog with this name, restart")
        main_function()


def list_of_dogs():
    print("Here are the list of dogs")

    # prints all the dogs in the roll on a new line
    for dog in roll:
        print(dog.title())
    main_function()


def calc_cost(number):
    COST_PER_DAY = 22.5  # Unsure why is does not like me using capitals??

    # testing to make use an integer is used
    valid = False
    while not valid:
        try:
            days = int(input("Enter number of days staying: "))
            valid = True
        except ValueError:
            print("Whoops, please enter an integer")

    total = number * days * COST_PER_DAY
    print(f"It costs ${total} for {number} dogs to stay for {days} days.")
    main_function()


def exit_program():
    print("End of Program, Goodbye!")


# Calling main function
print(f"{'--' * 10} Welcome to DogRus: a boarding house for dogs{'--' * 10}")
roll = []
main_function()
