from math import factorial
from functools import reduce

def add(x,y):
    """Returns the sum of x and y"""
    return x + y

def inverse(x):
    """Returns the reciprocal of x"""
    recip = 1/x
    return recip

def e(n):
    """Returns the approximation of e using a Taylor expansion"""
    list1 = list(range(n+1))
    list1 = list(map(factorial, list1))
    list1 = list(map(inverse, list1))
    eApprox = reduce(add, list1)
    return eApprox
