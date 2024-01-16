'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(totalVal, coins):
    """Returns a list whose first item is the minimum number of coins
    used to obtain a certain value (totalVal) and whose second item
    is a list of the coins in that optimal solution."""
    if coins[0] > coins[-1]:
        coins = coins[::-1]
    if totalVal == 0 or coins == []:
        return [0, []]
    elif len(coins) == 1:
        if coins[-1] > totalVal:
            return [0, []]
        else:
            x = giveChange(totalVal - coins[-1], coins)
            return [1 + x[0], [coins[-1]] + x[1]]
    elif coins[-1] > totalVal:
        return giveChange(totalVal, coins[:-1])
    else:
        x = giveChange(totalVal - coins[-1], coins)
        useIt = [1 + x[0], [coins[-1]] + x[1]]
        loseIt = giveChange(totalVal, coins[:-1])
        return min(useIt, loseIt)

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scoreList):
    """Returns the value associated with the given letter"""
    if letter == scoreList[0][0]:
        return scoreList[0][1]
    else:
        return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    """Returns the value of the given string S"""
    if len(S) > 0:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)
    else:
        return 0

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if len(dct) == 0:
        return []
    elif len(dct) == 1:
        return [[dct[0], wordScore(dct[0], scores)]]
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0 or len(L) == 0:
        return []
    else:
        return [L[0]] + take(n - 1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n > len(L):
        return []
    elif n == 0:
        return L
    else:
        return drop(n - 1, L[1:])
