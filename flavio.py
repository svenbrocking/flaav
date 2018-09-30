# flavio.py

import settings
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

# open file for reading
with open("msg_flavio.txt", "r") as msg_file:
    content = msg_file.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]


def kwartje(bot, update):
    """Send a random message when the command /kwartje is issued."""
    chatid = update.message.chat_id
    bot.send_chat_action(chat_id=chatid, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=chatid, text=random.choice(content))


def flv(bot, update):
    """Send a welcom message when the the bots name is issued."""
    txt = update.message.text.lower()
    if "fla" in txt:
        bot.send_message(chat_id=update.message.chat_id, text="Hey kwiebus!")


# create updater with api key
updater = Updater(TOKEN)

# get dispatcher to register handlers
dp = updater.dispatcher

# add handlers
dp.add_handler(CommandHandler("kwartje", kwartje))
dp.add_handler(MessageHandler(Filters.text, flv))

# start polling
updater.start_polling()
updater.idle()
