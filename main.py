import string
import random

# boardSize = 1
# minLen = 4
# maxLen = boardSize**2


def makeBoard(boardSize):
    board = []
    for i in range(boardSize):
        row = []
        for j in range(boardSize):
            letter = random.choice(string.ascii_lowercase)
            row.append(letter)
        board.append(row)
    return board

def printBoard(board):
    for row in board:
        print(" ".join(row).upper())

def isValidBoard(board):
    if not isinstance(board, list):
        return False
    for row in board:
        if len(row) != len(board):
            return False
        for item in row:
            if not isinstance(item, str):
                return False
            elif len(item) != 1:
                return False
    return True

# Returns a tuple (i, j) with new indices
def goLeft(size, i, j):
    if j < 1:
        return False
    else:
        return (i, j-1)

def goRight(size, i, j):
    if j >= (size - 1):
        return False
    else:
        return (i, j+1)

def goUp(size, i, j):
    if i < 1:
        return False
    else:
        return (i-1, j)

def goDown(size, i, j):
    if i >= (size - 1):
        return False
    else:
        return (i+1, j)

# Returns next letter in a certain direction, or empty string if direction is invalid
def goAdj(direction, board, starti, startj): 
    size = len(board)
    i = starti
    j = startj
    if direction=="upLeft":
        next = goUp(size, i, j)
        if next:
            (i, j) = next
            left = goLeft(size, i, j)
            if left:
                (i, j) = left
            else:
                return ""
        else: 
            return ""
    if direction=="up":
        next = goUp(size, i, j)
        if next:
            (i, j) = next
        else: 
            return ""
   
    return board[i][j]

def seek(board, starti, startj):
    minLen = 4
    maxLen = 4
    directions = ["upLeft", "up", "upRight",
                  "left", "right", "downLeft", 
                  "down", "downRight"]
    i = starti
    j = startj
    word = ""
    while len(word) < minLen:
        word += board[i][j]
        for d in directions:
            goAdj(d, board, i, j)
    return
        
#######

def test(size):
    b = makeBoard(size)
    printBoard(b)
    i = 1
    j = 1
    print(b[i][j])
    print(goLeft(b, i, j))
    print(goRight(b, i, j))
    print(goUp(b, i, j))
    print(goDown(b, i, j))

test(3)
