from django.contrib import admin

from contact.models import Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'first_name',
        'last_name',
        'email',
        'message',
    )

    ordering = ('created_at',)


admin.site.register(Message)