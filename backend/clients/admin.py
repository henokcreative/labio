from django.contrib import admin

# Register your models here.

from .models import Message, Contract

admin.site.register(Message)
admin.site.register(Contract)