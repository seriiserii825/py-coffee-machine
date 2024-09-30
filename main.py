#!/usr/bin/env python3
from modules.askUser import askUser
from modules.checkTransaction import checkTransaction
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
                    money_back = checkTransaction(coins, drink['cost'])
                    if money_back:
                        print(f"Here is your {choice}. Enjoy!")
                        data.money += drink['cost']
                        data.resources['water'] -= drink['ingredients']['water']
                        data.resources['coffee'] -= drink['ingredients']['coffee']
                        if 'milk' in drink['ingredients']:
                            data.resources['milk'] -= drink['ingredients']['milk']
                        if money_back > 0:
                            print(f"Here is ${money_back} in change.")

coffeeMachine()
