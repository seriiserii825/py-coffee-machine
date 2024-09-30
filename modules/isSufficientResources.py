from modules.data import resources, MENU


def isSufficientResources(choice):
    choice_ingredients = MENU[choice]['ingredients']
    for ingredient in choice_ingredients:
        if choice_ingredients[ingredient] > resources[ingredient]:
            print(f"[error]Not enough {ingredient}")
            return False
    return True
