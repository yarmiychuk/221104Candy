from random import randint as r

DEF_CANDIES = 150
DEF_MAX = 28
PLAYER_TURN = 0

candies: int = 0
isPlayerTurn: bool = None

def resetGame():
    global candies, isPlayerTurn
    candies = DEF_CANDIES
    isPlayerTurn = None
    pass

def changePlayer():
    global isPlayerTurn
    isPlayerTurn = r(0, 1) == PLAYER_TURN if isPlayerTurn == None else not isPlayerTurn
    return isPlayerTurn

def getMax():
    global candies
    maxGet = candies if candies <= DEF_MAX else DEF_MAX
    return maxGet

def botTakes():
    global candies
    if candies == 150:
        howToGet = r(1, DEF_MAX)
        candies -= howToGet
        return howToGet
    howToGet = candies
    if candies > DEF_MAX:
        howToGet = (candies - 1) % DEF_MAX
        if howToGet == 0:
            howToGet = r(1, DEF_MAX)
    candies -= howToGet
    return howToGet

def playerTakes(count: int):
    global candies
    candies -= count

def noGame():
    global candies, isPlayerTurn
    candies = 0
    isPlayerTurn = None