import telegram
from telegram import ChatAction, Update
from telegram.ext import CallbackContext
import json

from bot.main import bot
from bot.models import User, Word, Meaning

def user_update_or_create(update: Update):
    user, _ = User.objects.get_or_create(
        chat_id=update.message.chat_id,
        defaults={
            'role': User.Role.USER,
            'name': update.effective_user.name
        },
    )
    if user.name != update.effective_user.name:
        user.name = update.effective_user.name
        user.save()
    return user

def start(update: Update, context: CallbackContext):
    user = user_update_or_create(update)
    update.message.reply_text('Start')


def info(update: Update, context: CallbackContext):
    user = user_update_or_create(update)
    update.message.reply_text('Info')


def backup_words(update: Update, file_name='words'):
    words = Word.objects.all()
    update.message.reply_text(f'{len(words)} words found')
    if (len(words) == 0):
        return
    
    update.message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)
    file_name += '.json'
    with open(file_name, 'w') as file:
        json.dump(
            [{'text': word.text, 'type': word.type} for word in words], 
            file
        )    
    with open(file_name) as file:
        update.message.reply_document(file)

def backup_users(update: Update, file_name='users'):
    users = User.objects.all().iterator(500)   
    update.message.reply_text(f'{len(users)} users found')
    if (len(users) == 0):
        return

    update.message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)
    file_name += '.json'
    with open(file_name, 'w') as file:
        json.dump(
            [{'id': user.chat_id, 'role': user.role} for user in users], 
            file
        )
    with open(file_name) as file:
        update.message.reply_document(file)

def backup_meanings(update: Update, file_name='meanings'):
    meanings = Meaning.objects.all()
    update.message.reply_text(f'{len(meanings)} meanings found')
    if (len(meanings) == 0):
        return

    update.message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)
    file_name += '.json'
    with open(file_name, 'w') as file:
        json.dump(
            [{'text': meaning.text, 'word': meaning.word} for meaning in meanings],
            file
        )
    with open(file_name)) as file:
        update.message.reply_document(file)

def backup(update: Update, context: CallbackContext):
    user = user_update_or_create(update)
    if user.role != user.Role.ADMIN:
        update.message.reply_text('Command not recognized')
        return
    backup_users(update)
    backup_words(update)
    backup_meanings(update)



def echo(update: Update, context: CallbackContext):
    user = user_update_or_create(update)
    update.message.reply_text(update.message.text)
