def same(word):
    word = word.lower()
    if ((word)[0] == (word)[-1]):
        return True
    else:
        return False

def consecutiveSum(x, y):
    consSum = ((x + y)/2) * (y - x - 1)
    return(consSum)
