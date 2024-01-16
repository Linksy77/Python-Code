def change(amount, coins):
    """Returns the least amount of coins that makes up a certain amount of money"""
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[-1] > amount:
        return change(amount, coins[0 : -1])
    else:
        useIt = 1 + change(amount - coins[-1], coins)
        loseIt = change(amount, coins[0 : -1])
        return min(useIt, loseIt)
