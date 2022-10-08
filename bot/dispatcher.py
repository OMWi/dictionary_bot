from telegram.ext import (
    Dispatcher, MessageHandler,
    CommandHandler, Filters
)

from bot.main import bot
from dictionary_bot.settings import DEBUG
from bot.handlers import (
    start, info,
    backup, echo,
    test
)

def setup_dispatcher(dp: Dispatcher):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', info))
    return dp

n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers))