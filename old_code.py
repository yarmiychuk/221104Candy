# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as r

candies = 150
maxCount = 28

def getCurrentPlayer(p):
    if p == None:
        return r(1, 2)
    if p == 1:
        return 2
    return 1

numPlayers = int(input('Введите количество игроков (1-2): '))
currentPlayer = None
while candies > 0:
    currentPlayer = getCurrentPlayer(currentPlayer)
    print(f'Количество конфет на столе: {candies}')
    maxGet = candies
    if candies > maxCount:
        maxGet = maxCount
    if numPlayers == 1 and currentPlayer == 2:
        if (candies <= maxCount):
            howManyGet = candies
        else:
            howManyGet = (candies - 1) % maxCount
            if (howManyGet == 0):
                howManyGet = r(1, maxGet)
        print(f'Бот взял конфеты: {howManyGet} шт.')
        candies -= howManyGet
    else:
        while True:
            howManyGet = int(input(f'Сколько конфет берёт игрок {currentPlayer} (1-{maxGet}): '))
            if howManyGet > 0 and howManyGet <= maxGet:
                break
        candies -= howManyGet

# Result of game
if (numPlayers == 2):
    print(f'Победил игрок {currentPlayer}')
else:
    if (currentPlayer == 1):
        print('Вы победили!')
    else:
        print('Победил бот!')