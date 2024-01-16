def knapsack(capacity, itemList):
    """Returns the maximum value and the list of items that make this value, without exceeding the capacity of your knapsack"""
    if capacity <= 0 or itemList == []:
        return [0, []]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        x = knapsack(capacity - itemList[0][0], itemList[1:])
        useIt = [itemList[0][1] + x[0], [itemList[0]] + x[1]]
        loseIt = knapsack(capacity, itemList[1:])
        return max(useIt, loseIt)
