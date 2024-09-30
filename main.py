#!/usr/bin/env python3
from modules.askUser import askUser
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
            exit()
        elif choice == 'report':
            showReport()
        elif not choice in coffee_types:
            print(f"[red]Your choice not in coffee list")
        else:
            print(f"[red] Invalid choice")
            exit()

coffeeMachine()
