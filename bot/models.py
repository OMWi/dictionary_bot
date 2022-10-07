from django.db import models

class User(models.Model):
    chat_id = models.IntegerField()
    class Role(models.IntegerChoices):
        USER = 0
        ADMIN = 1
    role = models.IntegerField(choices=Role.choices)

class Word(models.Model):
    text = models.CharField(max_length=1024)
    class WordType(models.IntegerChoices):
        NOUN = 0
        PRONOUN = 1
        VERB = 2
        ADJECTIVE = 3
        ADVERB = 4
        PREPOSITION = 5
        CONJUCTION = 6
        INTERJECTION = 7
    type = models.IntegerField(choices=WordType.choices)

class Meaning(models.Model):
    text = models.CharField(max_length=1024)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)


