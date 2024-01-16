memoLuc = {}
memoCha = {}

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n == 0:
        memoLuc[(n)] = 2
        return memoLuc[(n)]
    elif n == 1:
        memoLuc[(n)] = 1
        return memoLuc[(n)]
    elif n in memoLuc:
        return memoLuc[(n)]
    else:
        memoLuc[(n)] = fast_lucas(n - 1) + fast_lucas(n - 2)
        return memoLuc[(n)]

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if amount == 0:
        memoCha[(amount)] = 0
        return memoCha[(amount)]
    elif coins == []:
        memoCha[(amount)] = float("inf")
        return memoCha[(amount)]
    elif coins[-1] > amount:
        memoCha[(amount)] = fast_change(amount, coins[0 : -1])
        return memoCha[(amount)]
    elif amount in memoCha:
        return memoCha[(amount)]
    else:
        useIt = 1 + fast_change(amount - coins[-1], coins)
        loseIt = fast_change(amount, coins[0 : -1])
        memoCha[(amount)] = min(useIt, loseIt)
        return memoCha[(amount)]

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

