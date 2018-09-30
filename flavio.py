#! python3
# flavio.py

from data.config import TOKEN

import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import data.mongo_setup as mongo_setup
import services.data_service as svc

# open file for reading
with open("msg_flavio.txt", "r") as msg_file:
    content = msg_file.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]


def kwartje(bot, update):
    """Send a random message when the command /kwartje is issued."""
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=chat_id, text=random.choice(content))


def flv(bot, update):
    """Send a welcome message when the the bots name is issued."""
    txt = update.message.text.lower()
    if "fla" in txt:
        bot.send_message(chat_id=update.message.chat_id, text="Hey kwiebus!")


def msg_create():
    svc.create_msg(content)


mongo_setup.global_init()

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
