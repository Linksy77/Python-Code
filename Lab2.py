def dot(L, K):
    """Returns the dot product of the lists L & K"""
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return L[0] * K[0]
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    """Returns a list of the characters of string S"""
    if len(S) == 0:
        return []
    if len(S) == 1:
        return [S[0]]
    else:
        return [S[0]] + explode(S[1:])

def ind(e, L):
    """Returns the index at which e is first found in L"""
    if L == [] or len(L) == 0:
        return len(L)
    if len(L) == 1:
        if L[0] == e:
            return 0
        else: return len(L)
    if L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e, L):
    """Returns a list identical to L except wihout all elements identical to e"""
    if len(L) == 0:
        return []
    if len(L) == 1:
        if L[0] != e:
            return [L[0]]
        else:
            return ""
    else:
        if L[0] != e:
            return [L[0]] + removeAll(e, L[1:])
        else:
            return removeAll(e, L[1:])

def myFilter(f, L):
    """Returns a list of all elements in list L that return True for the function f"""
    if len(L) == 0:
        return []
    if len(L) == 1:
        if f(L[0]) == True:
            return [L[0]]
        else:
            return []
    else:
        if f(L[0]) == True:
            return [L[0]] + myFilter(f, L[1:])
        else:
            return myFilter(f, L[1:])
 
def deepReverse(L):
    """Returns the reversal of list L, where, additionally, any element that is a list is also deepReversed"""
    if len(L) == 0:
        return []
    if len(L) == 1:
        if isinstance(L[-1], list):
            return [deepReverse(L[-1])]
        else:
            return [L[-1]]
    else:
        if isinstance(L[-1], list):
            return [deepReverse(L[-1])] + deepReverse(L[0 : -1])
        else:
            return [L[-1]] + deepReverse(L[0 : -1])
