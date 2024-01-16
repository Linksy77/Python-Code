from functools import reduce

def mult(x,y):
    """Returns the product of x and y"""
    return x * y

def factorial(n):
    """Returns the value of n!"""
    l1 = list(range(1, n+1))
    fact = reduce(mult, l1)
    return fact

def add(x,y):
    """Returns the sum of x and y"""
    return x + y

def mean(L):
    """Returns the mean (average) value of a list of integers"""
    listLength = len(L)
    listSum = reduce(add, L)
    return listSum / listLength
