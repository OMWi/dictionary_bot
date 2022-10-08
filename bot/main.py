from telegram import Bot

from dictionary_bot.settings import TG_TOKEN

bot = Bot(TG_TOKEN)
TG_BOT_USERNAME = bot.get_me()['username']
