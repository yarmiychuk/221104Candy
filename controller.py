from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import model, view

def start():
    model.noGame()
    app = ApplicationBuilder().token("5635697384:AAG5xXCaYDR4qtn7uM-B30Ep7ZFI7-tQh4U").build()
    app.add_handler(CommandHandler('start', view.hello))
    app.add_handler(CommandHandler('new', newGame))
    app.add_handler(CommandHandler('help', view.help))
    app.add_handler(CommandHandler('rules', view.rules))
    app.add_handler(MessageHandler(filters.TEXT, playerType))
    app.run_polling()

async def newGame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    model.resetGame()
    await nextTurn(update)

async def nextTurn(update: Update):
    if model.candies > 0:
        model.changePlayer()
        if model.isPlayerTurn:
            await view.askPlayerTurn(update, model.candies, model.getMax())
        else:
            await view.botTurn(update, model.candies, model.botTakes())
            await nextTurn(update)
    else:
        await endGame(update)

async def playerType(update, context):
    text = update.message.text
    if text == '/start' or text == '/new' or text == '/help' or text == '/rules':
        return
    if text.isnumeric() and model.candies > 0:
        count = int(text)
        if count == 0:
            await view.zero(update)
        elif count > model.getMax():
            await view.toMuch(update)
        else:
            model.playerTakes(count)
            await nextTurn(update)
    else:
        await view.wrongInput(update)

async def endGame(update: Update):
    await view.endGame(update, model.isPlayerTurn)
    model.noGame()