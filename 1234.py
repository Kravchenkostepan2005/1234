from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pprint import pprint

TOKEN = '5147834401:AAFIrq8GtNN5y8wg9LWxYKbXWa_4r4VaEsg'
updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher
print('Bot started. Press Ctrl+Z to exit')

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! Welcome to Calculator Bot!")


def any_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    if text.isdigit():
        number = float(text)
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    s = input("Enter s: ")
    if s == "+":
        print(a + b)
    elif s == "-":
        print(a - b)
    elif s == "*":
        print(a * b)
    elif s == "/":
        print(a / b)
    else:
        text = "Sorry, that doesn't look like a` number"
    context.bot.send_message(chat_id=chat.id, text=text)

dispatcher.add_handler(CommandHandler('start', start))   #/start
dispatcher.add_handler(MessageHandler(Filters.all, any_message))

updater.start_polling()
updater.idle()



def hello(text):
    pass
