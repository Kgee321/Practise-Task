"""Drop off Function being called -- Ask for name off dog and add it to the list
Katelyn Gee
15/03/2022
"""


def drop_off(roll):
    name = input("Enter the name of the dog being dropping off: ")
    print()
    roll.append(name)
    print("Dog has been dropped off")
    main_function()
