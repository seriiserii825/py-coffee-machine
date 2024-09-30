def checkTransaction(coins, price):
    print(f"coins: {coins}")
    print(f"price: {price}")
    if coins - price >= 0:
        result = round(coins - price, 2)
        print(f"result: {result}")
        return result
    else:
        print('Sorry that\'s not enough price. Money refunded.')
        return False
