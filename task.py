from building import building
from player import buildings
from logic import current_game_day as day

"""

TYPES OF TASK:

Type 0:
Description: Buy a loaf of bread from the bakery.
Building: Breadnik (2)

Type 1:
Description: Buy vegetables from the grocery shop.
Building: Grocerov (1)

Type 2:
Description: Buy household items from the grocery shop.
Building: Grocerov (1)

Type 3:
Description: Discuss the socio-political state of the world with Professor Ivanov.
Building: University (7)

Type 4:
Description: Check in with Comrade Kuznetsov.
Building: Stary Senat (8)

Type 5:
Description: Stay updated on the latest news from the Kremlin! Buy a transistor radio.
Building: Techno Store (6)

Type 6:
Description: You need to get moving! Buy a Lada.
Building: Lada DeaLership (5)

Type 7:
Description: It's that time of the week! Pay your bills.
Building: Gosbank (3)

Type 8:
Description: It's that time of the week! Pay your bills.
Building: Gosbank (3)

Type 9:
Description: Time to get on the property ladder. Take out a mortgage on your apartment.
Building: Gosbank (3)

Type 10:
Description: Nina sent you a covert message asking to meet to discuss secret business affairs.
Building: Nina's Bunker (5)

Type 11:
Description: Buy meat from the grocery shop.
Building: Grocerov (1)

Type 12:
Description: Buy Blini from the bakery.
Building: Breadnik (2)

"""
# list of prices associated with task type IDs
# if task does not require a purchase, this price is 0
tasks_cost_list = [8, 4, 6, 0, 0, 30, 80, 20, 16, 0, 0, 6, 1]
tasks_building_list = [2, 1, 1, 7, 8, 6, 5, 3, 3, 3, 5, 1, 2]
tasks_description_list = ["Buy a loaf of bread from the bakery.",
                          "Buy vegetables from the grocery shop.",
                          "Buy household items from the grocery shop."
                          "Discuss the socio-political state of the world with Professor Ivanov."
                          "Check in with Comrade Kuznetsov.",
                          "Stay updated on the latest news from the Kremlin! Buy a transistor radio.",
                          "You need to get moving! Buy a Lada.",
                          "It's that time of the week! Pay your bills.",
                          "It's that time of the week! Pay your bills.",
                          "Time to get on the property ladder. Take out a mortgage on your apartment.",
                          "Nina sent you a covert message asking to meet to discuss secret business affairs.",
                          "Buy meat from the grocery shop.",
                          "Buy Blini from the bakery."]

class task:
    def __init__(self, type_of_task):
        self.description = tasks_description_list[type_of_task]
        self.building = tasks_building_list[type_of_task]
        self.completed = False
        self.type = type
        self.cost = tasks_cost_list[type_of_task]


def generate_daily_tasks_list():
    tasks_list = []

    # first, regular/recurring tasks
    if day % 7 == 0:
        # Mondays
        tasks_list = [task(4), # check in with comrade
                      task(0)] # buy bread
    elif day % 7 == 1:
        # Tuesdays
        tasks_list = [task(2)] # buy household items
    elif day % 7 == 2:
        # Wednesdays
        tasks_list = [task(3)] # chat with prof
    elif day % 7 == 3:
        # Thursdays
        tasks_list = [task(1)] # buy vegetables
    elif day % 7 == 4:
        # Fridays
        if day % 14 == 4:
            tasks_list = [task(8)] # expensive bills
        elif day % 14 == 11:
            tasks_list = [task(7)] # cheaper bills
    elif day % 7 == 5:
        # Saturdays
        tasks_list = [task(12)] # buy Blini
    elif day % 7 == 6:
        # Sundays
        tasks_list = [task(11)] # buy meat
    
    # now adding one-off/game progression tasks
    if day == 8:
        tasks_list.append(task(5)) # buy radio
    if day == 12:
        tasks_list.append(task(10)) # take out mortgage
    if day == 14:
        tasks_list.append(task(6)) # buy car

    # return the array of task objects
    return(tasks_list)