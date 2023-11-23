# only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents
# coke costs 50
# 25, 10, 25, change owed to user should show 10
# Amount Due, Insert Coin, Change Owed

amount = 50
accept = [5, 10, 25]

while True:
    # loop these 2 onscreen effects
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))

    # if input does not match acceptable denomination, keep looping
    if not coin in accept:
        continue
    
    # else input matches acceptable denomination:
    else:
        amount = amount - coin
        # amount == 0
        if amount == 0:
            print(f"Change Owed: {amount}")
            break
        # amount < 0
        elif amount < 0:
            print(f"Change Owed: {-amount}")
            break





