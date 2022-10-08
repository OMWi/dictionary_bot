import telegram
from telegram import Update
from telegram.ext import CallbackContext
from bot.main import bot
from bot.models import User, Word, Meaning


def user_update_or_create(update: Update):
    user, _ = User.objects.update_or_create(
        chat_id=update.message.chat_id,
        defaults={
            'role': User.Role.USER,
            'name': update.effective_user.name
        },
    )
    return user


def start(update: Update, context: CallbackContext):
    print('start')
    user = user_update_or_create(update)
    update.message.reply_text('Start')


def info(update: Update, context: CallbackContext):
    print('info')
    user = user_update_or_create(update)
    update.message.reply_text('Info')

