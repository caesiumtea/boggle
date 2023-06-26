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

def isValidWord(word):
    minLen = 4
    maxLen = 4
    if len(word) >= minLen and len(word) <= maxLen:
        return True
    else:
        return False

# Returns a tuple (i, j) with new indices
def goLeft(i, j):
    if j < 1:
        return False
    else:
        return (i, j-1)

def goRight(i, j, size):
    if j >= (size - 1):
        return False
    else:
        return (i, j+1)

def goUp(i, j):
    if i < 1:
        return False
    else:
        return (i-1, j)

def goDown(i, j, size):
    if i >= (size - 1):
        return False
    else:
        return (i+1, j)

# Returns next letter in a certain direction, or empty string if direction is invalid
def goAdjacent(direction, board, starti, startj): 
    size = len(board)
    i = starti
    j = startj
    if direction=="upLeft":
        next = goUp(i, j)
        if next: #next will be False if already at top edge
            (i, j) = next
            left = goLeft(i, j)
            if left: #left will be False if already at left edge
                (i, j) = left
            else:
                return False
        else: 
            return False
    if direction=="up":
        next = goUp(i, j)
        if next:
            (i, j) = next
        else: 
            return False
    if direction=="upRight":
        next = goUp(i, j)
        if next:
            (i, j) = next
            right = goRight(i, j, size)
            if right: 
                (i, j) = right
            else:
                return False
        else: 
            return False
    if direction=="left":
        next = goLeft(i, j)
        if next:
            (i, j) = next
        else: 
            return False
    if direction=="right":
        next = goRight(i, j, size)
        if next:
            (i, j) = next
        else: 
            return False
    if direction=="downLeft":
        next = goDown(i, j, size)
        if next: 
            (i, j) = next
            left = goLeft(i, j)
            if left: 
                (i, j) = left
            else:
                return False
        else: 
            return False
    if direction=="down":
        next = goDown(i, j, size)
        if next:
            (i, j) = next
        else: 
            return False
    if direction=="downRight":
        next = goDown(i, j, size)
        if next:
            (i, j) = next
            right = goRight(i, j, size)
            if right: 
                (i, j) = right
            else:
                return False
        else: 
            return False
   
    return (i, j)

def addToWord(word, direction, board, i, j, maxLen):
    words = []
    next = True #initialize for the loop
    while next and len(word) <= maxLen: #next will be False if at the edge of board
        next = goAdjacent(direction, board, i, j)
        if next:
            i, j = next
        word += board[i][j]
        # if isValidWord(word):
        words.append(word)
    return words


def makeWords(board, starti, startj):
    minLen = 4
    maxLen = 4
    directions = ["upLeft", "up", "upRight",
                  "left", "right", 
                  "downLeft", "down", "downRight"]
    i = starti
    j = startj
    possibleWords = [] #includes non real words
    word = board[i][j]
    for d in directions:
        possibleWords += addToWord(word, d, board, i, j, maxLen)
        # i, j = goAdjacent(d, board, i, j) - no this is the wrong timing
        # get the last possible word returned and remove its last letter then try the other directions
        # but rn we dont have a way to get the i,j of the last letter
        # possibleWords += addToWord(word, d, board, i, j, maxLen)
    return possibleWords
        
#######

def test(size):
    b = makeBoard(size)
    printBoard(b)
    i = 1
    j = 1
    print(b[i][j])
    print(makeWords(b, 3, 3))

test(5)
