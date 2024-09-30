# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def processCoins():
    result = 0
    result += int(input("Insert quarters(0.25):")) * 0.25
    result += int(input("Insert quarters(0.10):")) * 0.1
    result += int(input("Insert quarters(0.05):")) * 0.05
    result += int(input("Insert quarters(0.01):")) * 0.01
    return result

