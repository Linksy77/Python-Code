def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 != 0:
        return True
    else:
        return False

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    else:
        rem = n % 2
        return numToBinary(n // 2) + str(rem)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        expNum = len(s) - 1
        binNum = int(s[0])
        return (binNum * (2**expNum)) + binaryToNum(s[1:])
    
def convToEight(stringNum):
    '''Helper function for increment function that converts a
    binary number less than 8 bits to 8 bits'''
    newNumLen = len(stringNum)
    if newNumLen < 8:
        stringNum = "0" + stringNum
        return convToEight(stringNum)
    else:
        return stringNum

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    newNum = numToBinary(binaryToNum(s) + 1)
    stringNum = str(newNum)
    newNumLen = len(stringNum)
    if s == "11111111":
        return "00000000"
    elif newNumLen < 8:
        return convToEight(stringNum)
    else:
        return stringNum

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
    else:
        print(s)
        return count(increment(s), n - 1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    else:
        rem = n % 3
        return numToTernary(n // 3) + str(rem)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        expNum = len(s) - 1
        terNum = int(s[0])
        return (terNum * (3**expNum)) + ternaryToNum(s[1:])
