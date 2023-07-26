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

# start from the top left letter and record every word going left to right
def naiveMakeWords1(board):
    size = len(board)
    words = []
    currentWord = ""
    i = 0
    j = 0
    currentWord += board[i][j]
    # initialize next for the loop
    next = True
    while next: 
        # next will be a tuple with indices of neighbor, unless it's already on 
        # the edge, in which case it will return False 
        next = goAdjacent("right", board, i, j)
        print(next)
        if next:
            # update i,j only if neighbor exists
            i, j = next
            currentWord += board[i][j]
        words.append(currentWord)
    return words

# start from an arbitrary letter instead
# also fix bug where last word gets added twice
def naiveMakeWords2(board, starti, startj):
    size = len(board)
    words = []
    i = starti
    j = startj
    currentWord = board[i][j]
    next = True
    while next:
        next = goAdjacent("right", board, i, j)
        print(next)
        if next:
            i, j = next
            currentWord += board[i][j]
            words.append(currentWord)
    return words
        
# this time, make it repeat for every direction
def naiveMakeWords3(board, starti, startj):
    size = len(board)
    directions = ["upLeft", "up", "upRight",
                  "left", "right", 
                  "downLeft", "down", "downRight"]
    i = starti
    j = startj
    words = []
    for d in directions:
        print(d)
        currentWord = board[i][j]
        next = True
        while next:
            next = goAdjacent(d, board, i, j)
            if next:
                i, j = next
                currentWord += board[i][j]
                words.append(currentWord)
        print(words)
    return words

# at this point we could call naiveMakeWords3 on every letter to get all words
# that can be found by going in a straight line
# how to get words that bend? use each of these words as a starting point and,
# for each one, iterate over the directions and add the next letters in that
# direction.
# but overall this approach seems wrong, getting every word along a single 
# direction... ideally we should have a function that adds just one letter

# look in one direction and add the next letter to a given word
# returns word and coordinates of where it ended
def addLetter(word, direction, board, starti, startj):
    i = starti
    j = startj
    next = goAdjacent(direction, board, i, j)
    if next:
        i, j = next
        word += board[i][j]
    return word, i, j

# want to try looping addLetter for each word in a list but the problem is
# needing to know where to start looking for each word
def extendWords(words, board):
    directions = ["upLeft", "up", "upRight",
                  "left", "right", 
                  "downLeft", "down", "downRight"]
    for word in words:
        for d in directions:
            addLetter(word, d, board, starti, startj)
    return words

# what if instead we stored words as a list of (i,j) tuples and then had a 
# function to convert the list of tuples into a word based on the board?
# the advantage is that we can use this to keep track of which letters have 
# already been included in this word and need to be skipped, as well as always 
# knowing where the word ends in order to know where to start when trying to 
# extend it


#######

def test(size):
    b = makeBoard(size)
    printBoard(b)
    #print(naiveMakeWords3(b, 0, 0))


test(5)
