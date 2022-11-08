from telegram import Update
from telegram.ext import ContextTypes

def getRulesText():
    message = 'На столе лежит 150 конфет. Мы будем брать конфеты по очереди, '
    message += 'но не более 28 штук за ход. Очередность первого хода определяется жеребьёвкой.\n'
    message += 'Победит тот, кто заберёт оставшиеся на столе конфеты последним.'
    return message

def getHelpText():
    message = '/new - начать новую игру\n'
    message += '/help - список команд\n/rules - правила игры'
    return message

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = f'Привет, {update.effective_user.first_name}!'
    message += ' Я хочу сыграть с тобой в одну игру...\n\n'
    message += getRulesText() + '\n\n' + getHelpText()
    await update.message.reply_text(message)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getHelpText())

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getRulesText())

def getEndOfWord(count: int):
    if count > 100:
        count -= 100
    if count > 4 and count < 21:
        return ''
    c = count % 10
    if c > 4 or c == 0:
        return ''
    elif c == 1:
        return 'а'
    return 'ы'

async def askPlayerTurn(update: Update, count: int, maxGet: int):
    await update.message.reply_text(f'На столе {count} конфет{getEndOfWord(count)}.\nТвой ход! Сколько конфет ты возьмёшь (1-{maxGet})?')

async def botTurn(update: Update, count: int, get: int):
    await update.message.reply_text(f'Осталось {count} конфет{getEndOfWord(count)}.\nЯ забираю {get}.')

async def zero(update: Update):
    await update.message.reply_text(f'Ты должен взять хотя бы одну конфету!')

async def toMuch(update: Update):
    await update.message.reply_text(f'Это слишком много, попробуй взять меньше.')

async def wrongInput(update: Update):
    await update.message.reply_text(f'Я не понимаю тебя. Попытайся ещё раз!')

async def endGame(update: Update, isPlayerWin: bool):
    await update.message.reply_text('На столе не осталось конфет...')
    if isPlayerWin:
        await update.message.reply_text('Что же, ты победил меня, поздравляю. Если хочешь сыграть ещё раз, набери команду /new')
    else:
        await update.message.reply_text('Я победил тебя. Если хочешь сыграть ещё раз, набери команду /new')