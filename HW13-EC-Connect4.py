class Board:

    def __init__(self, width=7, height=6):
        ''' Constructor for Board objects. Initializes width of board as
            7 and height of board as 6 if the user does not specify a
            custom width or height themselves.
        '''
        self.width = width
        self.height = height
        self.board = []
        for h in range(height):
            self.board.append([])
            for w in range(width):
                self.board[h].append(" ")

    def __str__(self):
        ''' Returns a string representing the Board object that calls it.
            Each "checker" takes up one space, and all columns are
            separated by vertical bars (|). The columns are labeled at the
            bottom.
        '''
        boardString = ""
        for h in range(self.height + 2):
            for w in range(self.width):
                if h != (self.height + 1) and h != (self.height):
                    if w != (self.width - 1):
                        if self.board[h][w] == " ":
                            boardString += "| "
                        elif self.board[h][w] == "X":
                            boardString += "|X"
                        elif self.board[h][w] == "O":
                            boardString += "|O"
                    else:
                        if self.board[h][w] == " ":
                            boardString += "| |\n"
                        elif self.board[h][w] == "X":
                            boardString += "|X|\n"
                        elif self.board[h][w] == "O":
                            boardString += "|O|\n"
                elif h == (self.height):
                    if w != (self.width - 1):
                        boardString += "-" * 2
                    else:
                        boardString += ("-" * 3) + "\n"
                elif h == (self.height + 1):
                    if w != (self.width - 1):
                        boardString += " " + str(w)
                    else:
                        boardString += " " + str(w) + " "
        return boardString

    def allowsMove(self, col):
        ''' Returns True if the calling Board object can allow a move
            into column c (because there is space available). Returns
            False is c does not have space available or if it is not
            a valid column.
            Essentially: checks to be sure that c is within the range
            from 0 to the last column and make sure that there is
            still room left in the column.
        '''
        col = int(col)
        if col in range(self.width): # Always returning False for whatever reason
            if self.board[0][col] != " ":
                return False
            else:
                return True
        else:
            return False

    def addMove(self, col, ox):
        ''' Adds an ox checker (where ox is a variable holding a string
            that is either "X" or "O") into column col.
        '''
        col = int(col)
        if self.allowsMove(col) == True:
            for h in range(self.height - 1, -1, -1):
                if self.board[h][col] == " ":
                    self.board[h][col] = ox
                    break

    def setBoard(self, move_string):
        ''' takes in a string of columns and places 
            alternating checkers in those columns, 
            starting with 'X' 
             
            For example, call b.setBoard('012345') 
            to see 'X's and 'O's alternate on the 
            bottom row, or b.setBoard('000000') to 
            see them alternate in the left column. 
 
            moveString must be a string of integers 
        '''
        nextCh = 'X'   # start by playing 'X' 
        for colString in move_string: 
            col = int(colString) 
            if 0 <= col <= self.width: 
                self.addMove(col, nextCh) 
            if nextCh == 'X': nextCh = 'O' 
            else: nextCh = 'X' 

    def winsFor(self, ox):
        ''' Returns True if the given checker, "X" or "O", held in ox,
            has won the calling Board. Returns False otherwise.
        '''
        if ox == "X":
            for h in range(self.height):
                for w in range(self.width):
                    if self.board[h][w] == "X":
                        if (self.width - (w + 1) >= 3) and (self.height - (h + 1) >= 3):
                            # Diagonal to the right win check
                            if self.board[h+1][w+1] == "X" and self.board[h+2][w+2] == "X" and self.board[h+3][w+3] == "X":
                                return True
                        if ((w + 1) >= 4) and (self.height - (h + 1) >= 3):
                            # Diagonal to the left win check
                            if self.board[h+1][w-1] == "X" and self.board[h+2][w-2] == "X" and self.board[h+3][w-3] == "X":
                                return True
                        if self.width - (w + 1) >= 3:
                            # Horizontal win check
                            if self.board[h][w+1] == "X" and self.board[h][w+2] == "X" and self.board[h][w+3] == "X":
                                return True
                        if self.height - (h + 1) >= 3:
                            # Vertical win check
                            if self.board[h+1][w] == "X" and self.board[h+2][w] == "X" and self.board[h+3][w] == "X":
                                return True
        elif ox == "O":
            for h in range(self.height):
                for w in range(self.width):
                    if self.board[h][w] == "O":
                        if (self.width - (w + 1) >= 3) and (self.height - (h + 1) >= 3):
                            # Diagonal to the right win check
                            if self.board[h+1][w+1] == "O" and self.board[h+2][w+2] == "O" and self.board[h+3][w+3] == "O":
                                return True
                        if ((w + 1) >= 4) and (self.height - (h + 1) >= 3):
                            # Diagonal to the left win check
                            if self.board[h+1][w-1] == "O" and self.board[h+2][w-2] == "O" and self.board[h+3][w-3] == "O":
                                return True
                        if self.width - (w + 1) >= 3:
                            # Horizontal win check
                            if self.board[h][w+1] == "O" and self.board[h][w+2] == "O" and self.board[h][w+3] == "O":
                                return True
                        if self.height - (h + 1) >= 3:
                            # Vertical win check
                            if self.board[h+1][w] == "O" and self.board[h+2][w] == "O" and self.board[h+3][w] == "O":
                                return True
        return False

    def hostGame(self):
        ''' Runs a loop allowing the user(s) to play a game of Connect Four
            when called from a connect four board object.
        '''
        won = False
        ox = "X"
        columnPos = None
        print("Welcome to Connect Four!\n")
        while won == False:
            print(self)
            print("\n")
            if ox == "X":
                columnPos = input("X's choice: ")
                print("\n")
                self.addMove(columnPos, ox)
                won = self.winsFor(ox)
                if won == True:
                    print("X wins -- Congratulations!\n")
                    print(self)
                ox = "O"
            elif ox == "O":
                columnPos = input("O's choice: ")
                print("\n")
                self.addMove(columnPos, ox)
                won = self.winsFor(ox)
                if won == True:
                    print("O wins -- Congratulations!\n")
                    print(self)
                ox = "X"

# b = Board()
# b.hostGame()
