# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

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

def convToNum(stringNum):
    '''Helper function that converts a
    binary number less than n bits to n bits'''
    return "0" * (5 - len(stringNum)) + stringNum

def compressHelp(S, lst):
    '''Helper function that returns an array  in the form ["0", 0],
    where the first element indicates whether a bit is 1 or 
    0 and the second element shows how long the string of 1s or 0s is.'''
    if S == "":
        return [lst]
    elif S[0] != lst[0] and lst[1] != 0:
        return [lst] + compressHelp(S[1:], [S[0]] + [1])
    return compressHelp(S[1:], [S[0]] + [lst[1] + 1])

def compressHelpTwo(lst):
    '''Helper function that takes the result from
    compressHelp(S, lst) and returns a binary string in base 10.
    If the consecutive 1 or 0 is larger than MAX_RUN_LENGTH,
    split.'''
    if lst == []:
        return ""
    if lst[0][1] > MAX_RUN_LENGTH:
        return "1111100000" + compressHelpTwo([[lst[0][0]] + [lst[0][1]-31]] + lst[1:])
    return convToNum(numToBinary(lst[0][1])) + compressHelpTwo(lst[1:])

def compress(S):
    '''Takes a binary string S of length 64 as input and returns another
    binary string as output, which should be a run-length encoding of the
    input string.'''
    if S[0] == "1":
        return "00000" + compressHelpTwo(compressHelp(S, ["0",0]))
    else:
        return compressHelpTwo(compressHelp(S, ["0", 0]))

def uncompressHelp(S):
    '''Helper function that uncompresses binary and returns a list of
    consecutive 0s and 1s.'''
    if S == "":
        return []
    else:
        return [binaryToNum(S[0 : COMPRESSED_BLOCK_SIZE])] + uncompressHelp(S[COMPRESSED_BLOCK_SIZE:])

def uncompressHelpTwo(lst, n):
    '''Helper function that takes the result from uncompressHelp(S) and
    returns the original binary string'''
    if lst == []:
        return ""
    elif n == True:
        return "0" * lst[0] + uncompressHelpTwo(lst[1:], not n)
    else:
        return "1" * lst[0] + uncompressHelpTwo(lst[1:], not n)
        

def uncompress(C):
    '''Does the opposite of the compress function (i.e. inverts/undoes the
    compressing done by the compress function).
    For example, uncompress(compress(S)) should return S.'''
    return uncompressHelpTwo(uncompressHelp(C), True)

def compression(S):
    '''Returns the ratio of the compressed size to the original size for
    image S.'''
    return len(compress(S)) / len(S)

"""[Explain what is the largest number of bits that the compress
algorithm could possibly use to encode a 64-bit string/image.]
"""

# The largest number of bits that the compress algorithm could
# possibly use to encode a 64-bit string/image is
# COMPRESSED_BLOCK_SIZE * 64 + COMPRESSED_BLOCK_SIZE. For example,
# given a string "10" * 32, due to the fact that the RLE starts with 0s,
# it will begin with "0" * COMPRESSED_BLOCK_SIZE (since there are no 0s,
# and then "0000100001", etc. to show that there is only one 1 and one 0.

"""
[Test your compression algorithm on several test images of your own design.
Describe the tests that you conducted and the compression ratios that you
found.]
"""

Penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
#print(compression(Penguin))
#Print statement returns 1.484375 as compression ratio for Penguin image.

Smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
#print(compression(Smile))
#Print statement returns 1.328125 as compression ratio for Smile image.
    
Five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
#print(compression(Five))
#Print statement returns 1.015625 as compression ratio for Five image.

"""
[Argue to NASA that Professor Lai is lying--such an algorithm cannot exist.
Try to make your reasoning as convincing and water-tight as possible.]
"""

'''
Given that there are specific cases in which the patterns of 0s and 1s may cause the
RLE to create a longer sequence than the one given (as was proven by the first question
and the previous examples), it is not possible for an algorithm such as the one that
Professor Lai is describing to exist.
'''
