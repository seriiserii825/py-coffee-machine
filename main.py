#!/usr/bin/env python3
from modules.askUser import askUser
from modules.isSufficientResources import isSufficientResources
from modules.processCoins import processCoins
from modules.showReport import showReport
from rich import print
from modules import data


def coffeeMachine():
    coffee_types = []
    for item in data.MENU:
        coffee_types.append(item)
    work_is_on = True
    while work_is_on:
        choice = askUser()
        if choice == 'off':
            print('[blue]Coffee machine is down')
            work_is_on = False
        elif choice == 'report':
            showReport()
        else:
            drink = data.MENU[choice]
            if isSufficientResources(drink['ingredients']):
                coins = processCoins()
                if coins != 0:
                    print(f"coins: {coins}")

coffeeMachine()
