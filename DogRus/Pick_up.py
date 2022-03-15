"""Create Pick_up function -- Asks for the name of the dog they are picking and
checks if it is in list.
Katelyn Gee
15/03/2022
 """


def pick_up(roll):
    name = input("Enter the name of the dog being picked up: ")
    if name in roll:
        roll.remove(name)
        print(f"{name} has been removed from the roll")
        main_fuction()
    else:
        print("There is no dog with this name, restart")
        main_function()
