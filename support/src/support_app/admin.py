from django.contrib import admin

from .models import Message, Ticket

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Message)
