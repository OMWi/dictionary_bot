from django.contrib import admin

from .models import User, Word, Meaning

admin.site.register(User)
admin.site.register(Word)
admin.site.register(Meaning)
