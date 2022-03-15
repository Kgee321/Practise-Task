"""call Calc_cost function -- ask the user for the number of days staying and tell them their cost
Katelyn Gee
15/03/2022"""


def calc_cost(number):
    days = int(input("Enter number of days staying: "))
    total = number * days * COST_PER_DAY
    print(f"It costs ${total} for {number} dogs to stay for {days} days.")
    main_function()
