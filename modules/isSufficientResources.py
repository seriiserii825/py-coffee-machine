from modules.data import resources, MENU


def isSufficientResources(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"[error]Not enough {ingredient}")
            return False
    return True
