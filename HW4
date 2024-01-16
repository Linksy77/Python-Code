memo = {}

def calcRow(currRow):
    '''Helper function to calculate a certain row in Pascal's Triangle'''
    if len(currRow) == 0:
        return []
    else:
        return [sum(currRow[:2])] + calcRow(currRow[1:])

def pascal_row(rowNum):
    '''Returns a list of elements found in a certain row of Pascal's Triangle'''
    if rowNum == 0:
        memo[(rowNum)] = [1]
        return [1]
    elif rowNum == 1:
        memo[(rowNum)] = [1] + pascal_row(rowNum - 1)
        return [1] + pascal_row(rowNum - 1)
    elif rowNum in memo:
        return memo[(rowNum)]
    else:
        memo[(rowNum)] = [1] + calcRow(pascal_row(rowNum - 1))
        return [1] + calcRow(pascal_row(rowNum - 1))

def pascal_triangle(n):
    '''Returns a list of the rows up to row n of Pascal's Triangle'''
    if n == 0:
        return [pascal_row(n)]
    else:
        return pascal_triangle(n - 1) + [pascal_row(n)]

def test_pascal_row():
    '''Function that takes no parameters and tests the function pascal_row'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]

def test_pascal_triangle():
    '''Function that takes no parameters and tests the function pascal_triangle'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
