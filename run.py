from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import os

TOKEN = os.environ['TOKEN']

def start(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
