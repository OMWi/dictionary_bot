from django.contrib import admin

from .models import User, Word, Meaning

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'name', 'role',)
    readonly_fields = ('chat_id',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('chat_id', 'name', 'role')
        }),
    )
admin.site.register(Word)


admin.site.register(Meaning)
