from django.contrib import admin
from core import models


@admin.register(models.EmailQueue)
class ConventionAdmin(admin.ModelAdmin):
    list_display = ('status', 'from_address', 'to_address', 'subject', 'body',
                    'when', 'when_sent')
