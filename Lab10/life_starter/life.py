#
# life.py - Game of Life lab
#
# Name: Cecilia Esteban
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    ''' Returns a 2D array with "height" rows and "width" cols '''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard( A ): 
    """ this function prints the 2d list-of-lists 
        A without spaces (using sys.stdout.write) 
    """ 
    for row in A: 
        for col in row: 
            sys.stdout.write( str(col) ) 
        sys.stdout.write( '\n' )

def diagonalize(width,height): 
    """ creates an empty board and then modifies it 
        so that it has a diagonal strip of "on" cells. 
    """ 
    A = createBoard( width, height ) 
     
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                A[row][col] = 1 
            else: 
                A[row][col] = 0      
    return A 

def innerCells(w, h):
    ''' Returns an array of all live cells - with the
        value 1 - except for a one-cell-wide border of
        empty cells (with the value of 0) around the
        edge of the 2D array.'''
    A = createBoard(w, h)
    rowCount = 0
    colCount = 0
    for row in range(h):
        colCount = 0
        for col in range(w):
            if (rowCount == 0 or colCount == 0) or (rowCount == h-1 or colCount == w-1):
                A[row][col] = 0
            else:
                A[row][col] = 1
            colCount += 1
        rowCount += 1
    return A

def randomCells(w, h):
    ''' Returns an array of randomy-assigned 1's and 0's
        except that the outer edge of the array is still
        completely empty (all 0's) as is the case of
        innerCells.
    '''
    A = createBoard(w, h)
    rowCount = 0
    colCount = 0
    for row in range(h):
        colCount = 0
        for col in range(w):
            if (rowCount == 0 or colCount == 0) or (rowCount == h-1 or colCount == w-1):
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
            colCount += 1
        rowCount += 1
    return A

def copy(A):
    ''' Makes a deep copy of the 2D array input.'''
    B = []
    for row in range(len(A)):
        rowAdd = []
        for col in range(len(A[row])):
            rowAdd.append(A[row][col])
        B.append(rowAdd)
    return B

def innerReverse(A):
    ''' Takes an old 2D array (or "generation") and
        then creates a new generation of the same shape
        and size, but where each cell of the new
        generation is the "opposite" of A's cells (with
        the exception of the outer edge, which remains 0
    '''
    newA = copy(A)
    for row in range(1, (len(newA)-1)):
        for col in range(1, (len(newA[row])-1)):
            if newA[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA

def countNeighbors(row,col,A):
    ''' Returns the number of live neighbors for a cell
        in the board A at a particular row and col.
    '''
    count = 0
    if A[row-1][col-1] == 1:
        count += 1
    if A[row-1][col] == 1:
        count += 1
    if A[row-1][col+1] == 1:
        count += 1
    if A[row][col-1] == 1:
        count += 1
    if A[row][col+1] == 1:
        count += 1
    if A[row+1][col-1] == 1:
        count += 1
    if A[row+1][col] == 1:
        count += 1
    if A[row+1][col+1] == 1:
        count += 1
    return count
        
        
def next_life_generation( A ): 
    """ makes a copy of A and then advanced one 
        generation of Conway's game of life within 
        the *inner cells* of that copy. 
        The outer edge always stays 0. 
    """
    newA = copy(A)
    for row in range(1, (len(A)-1)):
        for col in range(1, (len(A[row])-1)):
            neighbCount = countNeighbors(row, col, A)
            if neighbCount < 2 or neighbCount > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and neighbCount == 3:
                newA[row][col] = 1
    return newA

