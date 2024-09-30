from modules import data
from rich import print

def showReport():
    print(f"[green]Water: {data.resources['water']}ml")
    print(f"[blue]Milk: {data.resources['milk']}ml")
    print(f"[yellow]Coffee: {data.resources['coffee']}gr")
    print(f"[red]Money: ${data.money}")

