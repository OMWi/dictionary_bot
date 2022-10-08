from django.db import models

class User(models.Model):
    chat_id = models.IntegerField()
    name = models.CharField(max_length=128)
    class Role(models.IntegerChoices):
        USER = 0
        ADMIN = 1
    role = models.IntegerField(choices=Role.choices)

    def __str__(self):
        return f'{self.name}#{self.chat_id} {self.get_role_display()}'

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

    def __str__(self) -> str:
        return self.text

class Meaning(models.Model):
    text = models.CharField(max_length=1024)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text


